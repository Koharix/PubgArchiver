from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, tools
import PubgLogic


def func(pms):
    flow = flow_from_clientsecrets('client_secret_current.json', scope='https://www.googleapis.com/auth/spreadsheets')
    store = file.Storage('token.json')
    creds = tools.run_flow(flow, store)
    credentials = creds

    service = discovery.build('sheets', 'v4', credentials=credentials)

    # The ID of the spreadsheet to update.
    spreadsheet_id = '1rVvdlGiZKrYhBFq4oAFeVHTGwEZ322eQ2UNXvUL2NTw'  # TODO: Update placeholder value.

    # The A1 notation of a range to search for a logical table of data.
    # Values will be appended after the last row of the table.
    range_ = 'Sheet1!B2:Z'

    # How the input data should be interpreted.
    value_input_option = "RAW"

    # How the input data should be inserted.
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
