import json

class userInput:
    def __init__(self):
        pass
    def __init__(self, relFilePath):
        with open('userInput.json', 'r') as userInputFile:
            userInput = json.load(userInputFile)
            self.pubgApiKey = userInput["pubgApiKey"]
            self.spreadsheetId = userInput["spreadsheetId"]
    # def pubgApiKey(self):
    #     return self.pubgApiKey


