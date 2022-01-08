from datetime import datetime

import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint


def get_client():
    #Authorize the API
    scope = [
        'https://www.googleapis.com/auth/drive',
        'https://www.googleapis.com/auth/drive.file'
        ]
    file_name = 'client_key.json'
    creds = ServiceAccountCredentials.from_json_keyfile_name(file_name, scope)
    client = gspread.authorize(creds)
    return client


def get_sheet(client):
    #Fetch the sheet
    sheet = client.open('Ilihelpbot').sheet1
    return sheet
    # python_sheet = sheet.get_all_records()
    # pp = pprint.PrettyPrinter()
    # pp.pprint(python_sheet)


def save_note(note: str):
    client = get_client()
    sheet = get_sheet(client)
    sheet.insert_row([datetime.now().strftime("%d-%m-%y"), note])


client = get_client()
sheet = get_sheet(client)
