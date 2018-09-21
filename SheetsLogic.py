from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools

class SheetsLogic:
    def __init__(self, god):
        self.god = god

    def authenticate(self):
        flow = flow_from_clientsecrets('client_secret_current.json', scope='https://www.googleapis.com/auth/spreadsheets')
        store = file.Storage('token.json')
        return tools.run_flow(flow, store)

    def getService(self):
        return discovery.build('sheets', 'v4', credentials=self.authenticate())

    def getRecentMatchId(self):
        range_name = 'Sheet1!A1:A1'
        result = self.getService().spreadsheets().values().get(spreadsheetId=self.god.ui.spreadsheetId, range=range_name).execute()
        self.recentMatchId = result.get('values') if result.get('values') is not None else 0

    def setRecentMatchId(self):
        range_ = 'Sheet1!A1:A1'
        value_input_option = "RAW"
        value_range_body = {
            "range": range_,
            "values": [
                [self.god.ps.matchId]
            ]
        }
        request = self.getService().spreadsheets().values().update(spreadsheetId=self.god.ui.spreadsheetId, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()
        pprint(response)

    def appendPms(self):
        self.setRecentMatchId()
        range_ = 'Sheet1!B2:Z'
        value_input_option = "RAW"
        insert_data_option = "INSERT_ROWS"
        value_range_body = {
            "range": range_,
            "values": [
                self.god.ps.array
            ]
        }
        request = self.getService().spreadsheets().values().append(spreadsheetId=self.god.ui.spreadsheetId, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()
        pprint(response)
        self.setRecentMatchId()


