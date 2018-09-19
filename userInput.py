import json

class PMS:
    def __init__(self):
        pass
    def __init__(self, relFilePath):
        with open('userInput.json', 'r') as userInputFile:
            userInput = json.load(userInputFile)
            self.pubgApiTocken = userInput["pubgApiKey"]
            self.spreadsheetId = userInput["spreadsheetId"]


