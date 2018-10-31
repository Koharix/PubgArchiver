from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools
from google.oauth2 import service_account
import json

class SheetsLogic:
    def __init__(s, playerStats):
        s.service = s.getService()
        s.playerStats = playerStats
        with open('userInput.json', 'r') as uIF:
            s.spreadsheetId = json.load(uIF)["spreadsheetId"]

    def getService(s):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'googleCreds.json'
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        s.service = discovery.build('sheets', 'v4', credentials=credentials)

    def getRecentMatchId(s):
        rangeName = 'Sheet1!A1:A1'
        result = s.service.spreadsheets().values().get(spreadsheetId=s.spreadsheetId, range=rangeName).execute()
        recentMatchId = result.get('values') if result.get('values') is not None else 0
        return recentMatchId

    def setRecentMatchId(s, matchId):
        range = 'Sheet1!A1:A1'
        valueInputOption = "RAW"
        valueRangeBody = {
            "range": range,
            "values": [
                [matchId]
            ]
        }
        request = s.service.spreadsheets().values().update(spreadsheetId=s.spreadsheetId, range=range, valueInputOption=valueInputOption, body=valueRangeBody)
        response = request.execute()
        pprint(response)

    def appendPms(s, array):
        range = 'Sheet1!B2:Z'
        valueInputOption = "RAW"
        insert_data_option = "INSERT_ROWS"
        valueRangeBody = {
            "range": range,
            "values": [
                array
            ]
        }
        request = s.service.spreadsheets().values().append(spreadsheetId=s.spreadsheetId, range=range, valueInputOption=valueInputOption, insertDataOption=insert_data_option, body=valueRangeBody)
        response = request.execute()
        pprint(response)



