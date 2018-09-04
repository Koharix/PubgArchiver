from googleapiclient.discovery import build
from oauth2client import file, client, tools
from httplib2 import Http


SCOPES = 'https://www.googleapis.com/auth/spreadsheets.readonly'

# The ID and range of a sample spreadsheet
SAMPLE_SPREADSHEET_ID = '159s0s-4wW-XZPAOy_YUirpTXXybbDydGApaNqr46cTs'
SAMPLE_RANGE_NAME = 'Class Data!A2:E'

store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
    creds = tools.run_flow(flow, store)
service = build('sheets', 'v4', http=creds.authorize(Http()))
SPREADSHEET_ID = '159s0s-4wW-XZPAOy_YUirpTXXybbDydGApaNqr46cTs'
RANGE_NAME = 'Sheet1!A2:E'
result = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID,
                                            range=RANGE_NAME).execute()
values = result.get('values', [])

if not values:
    print('No data found.')
else:
    print('Name, Major:')
    for row in values:
        # Print columns A and E, which correspond to indices 0 and 4.
        print('%s, %s' % (row[0], row[3]))

