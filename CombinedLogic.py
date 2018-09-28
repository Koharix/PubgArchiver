import SheetsLogic
import PlayerStats
import PubgLogic

class CombinedLogic:
    def __init__(s):
        s.ps = PlayerStats.PlayerStats()
        s.pl = PubgLogic.PubgLogic()
        s.sl = SheetsLogic.SheetsLogic(s.ps)

    def storeRecentMatchs(s):
        s.pl.getPlayerInfo()
        storedRecentMatchId = s.sl.getRecentMatchId()
        matchIds = s.pl.getUnstoredMatchIds(storedRecentMatchId)
        print("HELLO THERE" + str(len(matchIds)))
        for matchId in matchIds:
            s.storeMatch(str(matchId))

    def storeMatch(s, matchId):
        s.ps.setMatchId(matchId)
        jsonMatchStats = s.pl.getMatchStats(matchId)
        jsonPlayerStats = s.pl.getPlayerMatchStats(jsonMatchStats)
        s.ps.storeMatchStats(jsonPlayerStats)
        s.sl.appendPms(matchId, s.ps.array)


