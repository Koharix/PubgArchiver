from oauth2client.client import flow_from_clientsecrets
from pprint import pprint
from googleapiclient import discovery
from oauth2client import file, client, tools
import Logic

clientId = '43373980248-oavlvs953r8vsjh3pq2q6og10jlmorer.apps.googleusercontent.com'
SCOPES = 'https://www.googleapis.com/auth/spreadsheets'
# relative = '/v4/spreadsheets/{spreadsheetId}/values/{range}:append'
# # The ID and range of a sample spreadsheet
# SAMPLE_SPREADSHEET_ID = '159s0s-4wW-XZPAOy_YUirpTXXybbDydGApaNqr46cTs'
# SAMPLE_RANGE_NAME = 'Class Data!A2:E'
#
# store = file.Storage('token.json')
# creds = store.get()
# if not creds or creds.invalid:
#     flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
#     creds = tools.run_flow(flow, store)
# service = build('sheets', 'v4', http=creds.authorize(Http()))
# SPREADSHEET_ID = '159s0s-4wW-XZPAOy_YUirpTXXybbDydGApaNqr46cTs'
# RANGE_NAME = 'Sheet1!A2:E'
# result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
#                                             range=RANGE_NAME).execute()
# values = result.get('values', [])
#
# if not values:
#     print('No data found.')
# else:
#     print('Name, Major:')
#     for row in values:
#         # Print columns A and E, which correspond to indices 0 and 4.
#         print('%s, %s' % (row[0], row[3]))
pms = Logic.getPlayerRecentMatchStat('Koharix')



# TODO: Change placeholder below to generate authentication credentials. See
# https://developers.google.com/sheets/quickstart/python#step_3_set_up_the_sample
#
# Authorize using one of the following scopes:
#     'https://www.googleapis.com/auth/drive'
#     'https://www.googleapis.com/auth/drive.file'
#     'https://www.googleapis.com/auth/spreadsheets'
flow = flow_from_clientsecrets('client_secret_current.json',
                               scope='https://www.googleapis.com/auth/spreadsheets')
store = file.Storage('token.json')
creds = tools.run_flow(flow, store)
credentials = creds

service = discovery.build('sheets', 'v4', credentials=credentials)

# The ID of the spreadsheet to update.
spreadsheet_id = '1rVvdlGiZKrYhBFq4oAFeVHTGwEZ322eQ2UNXvUL2NTw'  # TODO: Update placeholder value.

# The A1 notation of a range to search for a logical table of data.
# Values will be appended after the last row of the table.
range_ = 'Sheet1!A2:Z'  # TODO: Update placeholder value.

# How the input data should be interpreted.
value_input_option = 1  # TODO: Update placeholder value.

# How the input data should be inserted.
insert_data_option = '1'  # TODO: Update placeholder value.

value_range_body = {
    # TODO: Add desired entries to the request body.
}
value_range_body = pms
request = service.spreadsheets().values().append(spreadsheetId=spreadsheet_id, range=range_, valueInputOption=valueInputOption.RAW, insertDataOption=insert_data_option, body=value_range_body)
response = request.execute()

# TODO: Change code below to process the `response` dict:
pprint(response)
