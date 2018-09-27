

class CombinedLogic:
    def __init__(s):
        s.pl =
        s.sl =

    def storeRecentMatchs(s):
        s.god.pl.getPlayerInfo()
        storedRecentMatchId = s.god.sl.getRecentMatchId()
        matchIds = s.god.pl.getUnstoredMatchIds()
        for matchId in s.god.pl.matchIds:
            s.storeMatch(str(matchId))

    def storeMatch(s, matchId):
        s.god.pl.setMatchId(matchId)
        jsonMatchStats = s.god.pl.getMatchStats(matchId)
        jsonMatchStats = s.god.pl.getPlayerMatchStats(jsonMatchStats)
        s.god.pl.storePMSintoPMS(jsonMatchStats)
        s.god.sl.appendPms()


