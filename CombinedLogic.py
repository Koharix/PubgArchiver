import PubgLogic
import SheetsLogic

def storeRecentMatchs():
    storedRecentMatchId = SheetsLogic.getMostRecentMatchId()
    matchIds = PubgLogic.getUnstoredMatchIds(storedRecentMatchId)
    for matchId in matchIds:
        storeMatch(matchId)

def storeMatch(matchId):
    jsonMatchStats = PubgLogic.getMatchStats(matchId)
    jsonMatchStats = PubgLogic.getPlayerMatchStats(jsonMatchStats)
    PubgLogic.storePMSintoPMS(jsonMatchStats)
    pms = PubgLogic.getPms()
    SheetsLogic.appendPms(pms)
