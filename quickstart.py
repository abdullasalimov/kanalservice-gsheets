# import gspread
# import psycopg2

# from itertools import islice

# from googleapiclient.discovery import build
# from google.oauth2 import service_account

# from oauth2client.service_account import ServiceAccountCredentials

# # use creds to create a client to interact with the Google Drive API
# scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
# creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
# client = gspread.authorize(creds)

# # Find a workbook by name and open the first sheet
# # Make sure you use the right name here.
# sheet = client.open("Repositories Decoder").sheet1

# # data warehouse postgres db.
# dbhost = 'localhost' # replace if different
# dbuser = 'dbuser' # replace with actual database user
# dbpass = 'dbpassword' # replace with actual database password
# database = 'mydb' # replace with actual database name

# # port is 5432 by default.  So if different then specify port.
# dwarehouse_conn = psycopg2.connect(dbname=database, user=dbuser, host=dbhost, password=dbpass, port='5432')
# cursor = dwarehouse_conn.cursor()

# # Get number of rows in PostgreSQL table.
# repo_product_info_count_sql = 'SELECT COUNT(*) FROM repositories_product_information'
# cursor.execute(repo_product_info_count_sql)
# count_result = cursor.fetchone()

# # Number of rows in repositories_product_information from data warehouse.
# num_rows_repo_products = count_result[0]

# # This is a list of list of all data and wrap with length function to get row count.
# num_rows_sheets = len(sheet.get_all_values())

# # First row is the header to remove this from count.
# num_rows_sheets = num_rows_sheets - 1

# # Get results that can be iterated on.
# iterable_results = iter(sheet.get_all_values())
# # Skip header (first) row
# next(iterable_results)

# # islice is a library to allow us to slice or start iterating in loop
# # from a certain number.  In this case, we start at the last row already
# # inserted into the PostgreSQL table.  So if the PostgreSQL table has 5 entries (row count of 5)
# # then we start looping through the Google Sheet at that number to prevent inserting duplicates.
# # This is, of course, assuming the database only has rows getting inserted from the spreadsheet.
# # @todo: may remove islice and update code with insert/update based on referer.
# for i, value in islice(enumerate(iterable_results), num_rows_repo_products, None):
#     # value[0], the referer url cannot be null or empty so skip this row if it is.
#     if not value[0]:
#         continue
#     referer = value[0]
#     hardware_platform = "" if not value[1] else value[1]
#     os = "" if not value[2] else value[2]
#     os_version = "" if not value[3] else value[3]
#     product_name = "unknown" if not value[4] else value[4]
#     product_version = "" if not value[5] else value[5]
#     packaging = "" if not value[6] else value[6]
#     campaign = "" if not value[7] else value[7]

#     # Build insert query and insert records from spreadsheet into PostgreSQL table.
#     query = (
#         "INSERT INTO repositories_product_information (referer, hardware_platform, os, os_version, product, product_version, packaging, campaign_id)"
#         "VALUES (%s, %s, %s, %s, %s, %s, %s, %s)")
#     cursor.execute(query, (
#         referer, hardware_platform, os, os_version, product_name, product_version, packaging, campaign))
#     dwarehouse_conn.commit()

#     print value




import gspread
import psycopg2

CREDINTIANAL = 'keys.json'
SAMPLE_SPREADSHEET_ID = '1Z38ZTvYry5glASyyytFY4FcTB_ckiXcMWPN7b9lRZSM'

gc = gspread.service_account(CREDINTIANAL)
sh = gc.open_by_key(SAMPLE_SPREADSHEET_ID)

worksheet = sh.sheet1

list_of_dicts = worksheet.get_all_records()


#data postgres db
dbhost = 'localhost'
dbuser = 'postgres'
dbpass = '123'
database = 'mydb'
dbport = '5432'

data_conn = psycopg2.connect(dbname=database, user=dbuser, host=dbhost, password=dbpass, port=dbport)
cursor = data_conn.cursor()

#


service.files().get(fileId='1Z38ZTvYry5glASyyytFY4FcTB_ckiXcMWPN7b9lRZSM', fields="modifiedTime").execute()






# # Google sheets api

# # from googleapiclient.discovery import build
# # from google.oauth2 import service_account

# # SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
# # SERVICE_ACCOUNT_FILE = 'keys.json'

# # SAMPLE_SPREADSHEET_ID = '1Z38ZTvYry5glASyyytFY4FcTB_ckiXcMWPN7b9lRZSM'
# # SAMPLE_RANGE_NAME = 'Лист1!B2:D1000'

# # creds = None
# # creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # service = build('sheets', 'v4', credentials=creds)

# # sheet = service.spreadsheets()
# # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=SAMPLE_RANGE_NAME).execute()
# # values = result.get('values', [])



# # from googleapiclient.discovery import build
# # from google.oauth2 import service_account

# # SERVICE_ACCOUNT_FILE = 'keys.json'
# # SCOPES = ['https://www.googleapis.com/auth/drive.metadata']

# # creds = None
# # creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)

# # service = build('drive', 'v3', credentials=creds)

# # print(service.about().get(fields='modifiedTime').execute())





# # file_id = '1Z38ZTvYry5glASyyytFY4FcTB_ckiXcMWPN7b9lRZSM'

# # a = service.files().get_media(fileId=file_id)

# # print(a)

# # # Call the Drive v3 API
# # results = service.files().list(pageSize=10, fields="nextPageToken, files(id, name)").execute()
# # items = results.get('files', [])
# # print(items)




# ############################
# '''
# import traceback
# import urllib3
# import xmltodict

# def getxml():
#     url = "https://www.cbr.ru/scripts/XML_daily.asp?"

#     http = urllib3.PoolManager()

#     response = http.request('GET', url)
#     try:
#         data = xmltodict.parse(response.data)
#     except:
#         print("Failed to parse xml from response (%s)" % traceback.format_exc())
#     return data
# '''
# #########################
# # import psycopg2

# # #establishing the connection
# # conn = psycopg2.connect(
# #    database="postgres", user='postgres', password='123', host='127.0.0.1', port= '5432'
# # )
# # conn.autocommit = True

# # #Creating a cursor object using the cursor() method
# # cursor = conn.cursor()

# # #Preparing query to create a database
# # sql = '''CREATE database mydb''';

# # #Creating a database
# # cursor.execute(sql)
# # print("Database created successfully........")

# # #Closing the connection
# # conn.close()

