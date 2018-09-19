import PubgLogic
import SheetsLogic
import userInput

class CombinedLogic:
    def __init__(self, god):
        self.god = god


    def storeRecentMatchs(self, player):
        self.god.pl.getPlayerInfo(player)
        storedRecentMatchId = self.god.sl.getRecentMatchId()
        matchIds = self.god.pl.getUnstoredMatchIds(storedRecentMatchId)
        for matchId in matchIds:
            self.storeMatch(str(matchId))

    def storeMatch(self, matchId):
        self.god.pl.setMatchId(matchId)
        jsonMatchStats = self.god.pl.getMatchStats(matchId)
        jsonMatchStats = self.god.pl.getPlayerMatchStats(jsonMatchStats)
        self.god.pl.storePMSintoPMS(jsonMatchStats)
        pms = self.god.pl.getPms()
        self.god.sl.appendPms(pms)


