from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render

from currency.models import Data

from datetime import datetime

# Google API
from google.oauth2 import service_account
from googleapiclient.discovery import build

# XML to JSON
import traceback
import urllib3
import xmltodict


CREDENTIAL = 'keys.json'
FILE_ID = '1Z38ZTvYry5glASyyytFY4FcTB_ckiXcMWPN7b9lRZSM'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets', 'https://www.googleapis.com/auth/drive.metadata']
SAMPLE_RANGE_NAME = '!B2:D1000'


def last_modified_date_spreadsheet():

    creds = None
    creds = service_account.Credentials.from_service_account_file(settings.CREDENTIAL, scopes=settings.SCOPES)

    # get last modified date of spreadsheet
    service = build('drive', 'v3', credentials=creds)
    last_modified_date = service.files().get(fileId=settings.FILE_ID, fields="modifiedTime").execute() 
    
    return last_modified_date['modifiedTime']


def currency_rub():
    url = "https://www.cbr.ru/scripts/XML_daily.asp?"
    http = urllib3.PoolManager()
    response = http.request('GET', url)
    try:
        data = xmltodict.parse(response.data)
    except:
        print("Failed to parse xml from response (%s)" % traceback.format_exc())
    return data['ValCurs']['Valute'][10]['Value']


def index(request):
    
    last_date_gsheets = last_modified_date_spreadsheet()

    try:
        last_record_db = Data.objects.latest('updated_at').updated_at.strftime('%Y-%m-%dT%H:%M:%SZ')
    except:
        last_record_db = ''

    if (last_record_db == '') or (last_record_db < last_date_gsheets):
        creds = None
        creds = service_account.Credentials.from_service_account_file(settings.CREDENTIAL, scopes=settings.SCOPES)

        service = build('sheets', 'v4', credentials=creds)
        sheet = service.spreadsheets()
        result = sheet.values().get(spreadsheetId=settings.FILE_ID, range=settings.SAMPLE_RANGE_NAME).execute()
        values = result.get('values', [])

        

        for value in values:
            date = datetime.strptime(value[2], "%d.%m.%Y")
            Data(order_number=value[0], price_usd=value[1], delivery_date=date).save()
        
        queryset = Data.objects.all()
        
        return render(request, 'index.html', {'queryset':queryset})

    else:
        queryset = Data.objects.all()
        
        return render(request, 'index.html', {'queryset':queryset})


    # gc = gspread.service_account(CREDS)
    # sh = gc.open_by_key(FILE_ID)

    # worksheet = sh.sheet1

    # list_of_dicts = worksheet.get_all_values()
    # del(list_of_dicts[0])

    # values = Data.objects.all()

    # if list_of_dicts == values:
    #     return render(request, 'index.html', context={'values':list_of_dicts})
    
    # else:
    #     return render(request, 'index.html')