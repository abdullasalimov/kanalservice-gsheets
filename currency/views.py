from django.conf import settings
from django.shortcuts import render

from currency.models import Data

from datetime import datetime

import requests

# Google API
from google.oauth2 import service_account
from googleapiclient.discovery import build

# XML to JSON
import traceback
import urllib3
import xmltodict


def send_notification_telegram(order_numbers=[]):
    messages = []
    users_id = []

    for order in order_numbers:
        messages.append(order.order_number)
    
    url_users_id = f"https://api.telegram.org/bot{settings.TOKEN}/getUpdates"

    for user in requests.get(url_users_id).json()['result']:
        users_id.append(user['message']['chat']['id'])
    
    users_id = list(dict.fromkeys(users_id))
    
    message = f"Срок поставки истек для следующих заказов: {messages}"
    for user_id in users_id:
        url = f"https://api.telegram.org/bot{settings.TOKEN}/sendMessage?chat_id={user_id}&text={message}"
        requests.get(url).json()


def currency_rub():
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data['ValCurs']['Valute'][10]['Value']


def index(request):
    creds = None
    creds = service_account.Credentials.from_service_account_file(settings.CREDENTIAL, scopes=settings.SCOPES)
    service = build('sheets', 'v4', credentials=creds)
    sheet = service.spreadsheets()
    result = sheet.values().get(spreadsheetId=settings.FILE_ID, range=settings.SAMPLE_RANGE_NAME).execute()
    values = result.get('values', [])

    for value in values:
        data, created = Data.objects.update_or_create(order_number=value[1], defaults={
            'seq_number':int(value[0]), 
            'price_usd': value[2], 
            'delivery_date': datetime.strptime(value[3], "%d.%m.%Y"), 
            'price_rub': "{:.2f}".format(float(value[2])*float(currency_rub().replace(",", ".")))
            }
        )

    
    queryset = Data.objects.order_by('seq_number')

    outdated_delivery = Data.objects.filter(delivery_date__lt=datetime.today())

    send_notification_telegram(outdated_delivery)

    return render(request, 'index.html', {'queryset':queryset})
    