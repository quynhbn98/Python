# from google.auth.transport.requests import Request
# from google.oauth2.credentials import Credentials
# from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.errors import HttpError
from googleapiclient.discovery import build
from google.oauth2 import service_account
import pandas as pd
import socket

timeout_in_sec = 60*3 # 3 minutes timeout limit
socket.setdefaulttimeout(timeout_in_sec)

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
SERVICE_ACCOUNT_FILE = 'keys.json'

creds = service_account.Credentials.from_service_account_file(SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

def google_sheet_read(spreadsheetId, range):
    result = sheet.values().get(spreadsheetId=spreadsheetId, range=range).execute()
    values = result.get('values', [])
    return values

def google_sheet_write(spreadsheetId, range, body, valueInputOption = 'USER_ENTERED'):
    request = sheet.values().update(
        spreadsheetId=spreadsheetId, 
        range = range,
        valueInputOption = valueInputOption,
        body = body
        )
    response = request.execute()
    return response

def google_sheet_add_empty(spreadsheetId, sheetId, dimension = 'ROWS', startIndex = 0, numAdded = 1):
    request = service.spreadsheets().batchUpdate(
        spreadsheetId = spreadsheetId, 
        body = {
            "requests": [
                {
                "insertDimension": {
                    "range": {
                    "sheetId": sheetId,
                    "dimension": dimension,
                    "startIndex": startIndex,
                    "endIndex": startIndex + numAdded
                    },
                    "inheritFromBefore": False
                }
                }
            ]
        }
    )
    response = request.execute()
    return response

def google_sheet_clear(spreadsheetId, range, body={}):
    request = service.spreadsheets().values().clear(
        spreadsheetId = spreadsheetId, 
        range = range,
        body = body
    )
    response = request.execute()
    return response

# file = '1FQL-C4sdbbJPHYSAFo8nzu805FDZOyvetLvzgy1c6EQ'
# sheet = 1047904116
# google_sheet_add_empty(file, sheet, startIndex=1)

# # read data
# result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                             range='Nháp!A1:A7').execute()
# values = result.get('values', [])
# print(values)

# # update data
# request = sheet.values().update(
#     spreadsheetId=SAMPLE_SPREADSHEET_ID, 
#     range = 'Nháp!A1',
#     valueInputOption = 'USER_ENTERED',
#     body = {'values':[['a','b'],['c']]}
#     )
# response = request.execute()

# https://medium.com/@harshit4084/track-your-loop-using-tqdm-7-ways-progress-bars-in-python-make-things-easier-fcbbb9233f24