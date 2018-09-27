from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools
import json

class SheetsLogic:
    def __init__(s, relFilePath, ps):
        s.ps = ps
        with open('userInput.json', 'r') as uIF:
            s.sId = json.load(uIF)["spreadsheetId"]

    def authenticate(s):
        flow = flow_from_clientsecrets('client_secret_current.json', scope='https://www.googleapis.com/auth/spreadsheets')
        store = file.Storage('token.json')
        return tools.run_flow(flow, store)

    def getService(s):
        return discovery.build('sheets', 'v4', credentials=s.authenticate())

    def getRecentMatchId(s):
        range_name = 'Sheet1!A1:A1'
        result = s.getService().spreadsheets().values().get(spreadsheetId=s.sId, range=range_name).execute()
        s.recentMatchId = result.get('values') if result.get('values') is not None else 0
        return s.recentMatchId

    def setRecentMatchId(s):
        range_ = 'Sheet1!A1:A1'
        value_input_option = "RAW"
        value_range_body = {
            "range": range_,
            "values": [
                [s.ps.matchId]
            ]
        }
        request = s.getService().spreadsheets().values().update(spreadsheetId=s.sId, range=range_, valueInputOption=value_input_option, body=value_range_body)
        response = request.execute()
        pprint(response)

    def appendPms(s):
        s.setRecentMatchId()
        range_ = 'Sheet1!B2:Z'
        value_input_option = "RAW"
        insert_data_option = "INSERT_ROWS"
        value_range_body = {
            "range": range_,
            "values": [
                s.ps.array
            ]
        }
        request = s.getService().spreadsheets().values().append(spreadsheetId=s.sId, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
        response = request.execute()
        pprint(response)
        s.setRecentMatchId()


