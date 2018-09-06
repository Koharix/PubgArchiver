from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools

spreadsheet_id = '1rVvdlGiZKrYhBFq4oAFeVHTGwEZ322eQ2UNXvUL2NTw'

def authenticate():
    flow = flow_from_clientsecrets('client_secret_current.json', scope='https://www.googleapis.com/auth/spreadsheets')
    store = file.Storage('token.json')
    return tools.run_flow(flow, store)

def getService():
    return discovery.build('sheets', 'v4', credentials=authenticate())

def getMostRecentMatchId():
    range_name = 'Sheet1!A1:A1'
    result = getService().spreadsheets().values().get(spreadsheetId=spreadsheet_id, range=range_name).execute()
    numRows = result.get('values') if result.get('values') is not None else 0
    print(numRows)

def storeRecentMatchId():
    pass

def appendPms(pms):
    range_ = 'Sheet1!B2:Z'
    value_input_option = "RAW"
    insert_data_option = "INSERT_ROWS"
    value_range_body = {
        "range": range_,
        "values": [
            pms.array
        ]
    }
    request = getService().spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()
    pprint(response)

