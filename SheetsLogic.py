from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools

def authenticate():
    flow = flow_from_clientsecrets('client_secret_current.json', scope='https://www.googleapis.com/auth/spreadsheets')
    store = file.Storage('token.json')
    return tools.run_flow(flow, store)

def storePms(pms):
    service = discovery.build('sheets', 'v4', authenticate())
    spreadsheet_id = '1rVvdlGiZKrYhBFq4oAFeVHTGwEZ322eQ2UNXvUL2NTw'
    range_ = 'Sheet1!B2:Z'
    value_input_option = "RAW"
    insert_data_option = "INSERT_ROWS"
    value_range_body = {
        "range": range_,
        "values": [
            pms.array
        ]
    }
    request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=value_input_option, insertDataOption=insert_data_option, body=value_range_body)
    response = request.execute()
    pprint(response)

def getMostRecentMatch():
    pass