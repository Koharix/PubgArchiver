

class CombinedLogic:
    def __init__(self, god):
        self.god = god


    def storeRecentMatchs(self, player):
        self.god.pl.getPlayerInfo()
        storedRecentMatchId = self.god.sl.getRecentMatchId()
        matchIds = self.god.pl.getUnstoredMatchIds()
        for matchId in self.god.pl.matchIds:
            self.storeMatch(str(matchId))

    def storeMatch(self, matchId):
        self.god.pl.setMatchId(matchId)
        jsonMatchStats = self.god.pl.getMatchStats(matchId)
        jsonMatchStats = self.god.pl.getPlayerMatchStats(jsonMatchStats)
        self.god.pl.storePMSintoPMS(jsonMatchStats)
        self.god.sl.appendPms()


