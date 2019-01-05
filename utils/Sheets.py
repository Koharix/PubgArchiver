from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools
from google.oauth2 import service_account
import json


class SheetsLogic:
    def __init__(self, playerStats):
        self.service = self.get_service()
        self.playerStats = playerStats
        with open('userInput.json', 'r') as uIF:
            self.spreadsheetId = json.load(uIF)["spreadsheetId"]

    def get_service(self):
        SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
        SERVICE_ACCOUNT_FILE = 'googleCreds.json'
        credentials = service_account.Credentials.from_service_account_file(
            SERVICE_ACCOUNT_FILE, scopes=SCOPES)
        self.service = discovery.build('sheets', 'v4', credentials=credentials)

    def get_recent_match_id(self):
        rangeName = 'Sheet1!A1:A1'
        result = self.service.spreadsheets().values().get(spreadsheetId=self.spreadsheetId, range=rangeName).execute()
        recentMatchId = result.get('values') if result.get('values') is not None else 0
        return recentMatchId

    def set_recent_match_id(self, matchId):
        range = 'Sheet1!A1:A1'
        valueInputOption = "RAW"
        valueRangeBody = {
            "range": range,
            "values": [
                [matchId]
            ]
        }
        request = self.service.spreadsheets().values().update(spreadsheetId=self.spreadsheetId,
                                                              range=range,
                                                              valueInputOption=valueInputOption,
                                                              body=valueRangeBody)
        response = request.execute()
        pprint(response)

    def append_pms(self, array):
        range = 'Sheet1!B2:Z'
        valueInputOption = "RAW"
        insert_data_option = "INSERT_ROWS"
        valueRangeBody = {
            "range": range,
            "values": [
                array
            ]
        }
        request = self.service.spreadsheets().values().append(spreadsheetId=self.spreadsheetId,
                                                              range=range,
                                                              valueInputOption=valueInputOption,
                                                              insertDataOption=insert_data_option,
                                                              body=valueRangeBody)
        response = request.execute()
        pprint(response)



