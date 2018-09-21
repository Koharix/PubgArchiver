import json

class UserInput:
    def __init__(self):
        pass

    def __init__(self, god):
        self.god = god

    def __init__(self, god, relFilePath):
        self.god = god
        with open('userInput.json', 'r') as userInputFile:
            userInput = json.load(userInputFile)
            self.pubgApiKey = userInput["pubgApiKey"]
            self.spreadsheetId = userInput["spreadsheetId"]
            self.player1 = userInput["player1"]
            self.player2 = userInput["player2"]
            self.region = userInput["region"]


