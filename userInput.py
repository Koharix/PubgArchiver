import json

class userInput:
    def __init__(self):
        pass
    def __init__(self, relFilePath):
        with open('userInput.json', 'r') as userInputFile:
            userInput = json.load(userInputFile)
            self.pubgApiKey = userInput["pubgApiKey"]
            self.spreadsheetId = userInput["spreadsheetId"]
            self.player1 = userInput["player1"]
            self.player2 = userInput["player2"]
    # def pubgApiKey(self):
    #     return self.pubgApiKey


