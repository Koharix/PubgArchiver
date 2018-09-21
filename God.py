import userInput
import PubgLogic
import SheetsLogic
import CombinedLogic
import PlayerStats

class God:
    def __init__(self):
        self.ui = userInput.userInput(self, 'userInput.json')
        self.pl = PubgLogic.PubgLogic(self)
        self.sl = SheetsLogic.SheetsLogic(self)
        self.cl = CombinedLogic.CombinedLogic(self)
        self.ps = PlayerStats.PlayerStats(self)
