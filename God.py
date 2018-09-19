import userInput
import PubgLogic
import SheetsLogic
import PMS

class God:
    def __init__(self):
        self.ui = userInput.userInput(userInput.json)
        self.pl = PubgLogic.PubgLogic()
        self.sl = SheetsLogic.SheetsLogic(self)
