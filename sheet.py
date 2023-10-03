import io
import json
import os
from google.auth.transport.requests import Request
from google.oauth2.service_account import Credentials
from googleapiclient.discovery import build

def update_google_sheet_data(google_sheet_link, worksheet_name, data,api_key, range=None):

  # Create a service account object.
  credentials = Credentials.from_service_account_file("/content/starry-antonym-396712-9eb1035049c1.json")

  # Create a Google Sheets API object.
  sheets_service = build("sheets", "v4", credentials=credentials)

  # Get the spreadsheet ID from the Google Sheet link.
  spreadsheet_id = google_sheet_link.split("/")[5]
  print(spreadsheet_id)

  # Update the data in the Google Spreadsheet.
  body = {
    "values": data
  }

  if range is not None:
    request = sheets_service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range=range, valueInputOption="RAW", body=body,key=api_key)
  else:
    request = sheets_service.spreadsheets().values().update(spreadsheetId=spreadsheet_id, range="A2:Z", valueInputOption="RAW", body=body,key=api_key)

  request.execute()

# Example usage:

google_sheet_link = "https://docs.google.com/spreadsheets/d/1Hwvm7Ngd-f91xW15Pg4otklNLM8ufV2dV-dq5dbBGL4/edit?usp=sharing"
worksheet_name = "Sheet1"
data = [['26/10/2023', "hye data", 'URL'], ['28/10/2023', "hye data", 'URL'], ['29/10/2023', "hye data", 'URL']]

update_google_sheet_data(google_sheet_link, worksheet_name, data,api_key= "AIzaSyC_uLVIPUvgufbfx7011sx-NwyGL0okZBQ")
