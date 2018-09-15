import PubgLogic
import SheetsLogic

def storeRecentMatchs(player):
    PubgLogic.getPlayerInfo(player)
    storedRecentMatchId = SheetsLogic.getRecentMatchId()
    print((storedRecentMatchId))
    matchIds = PubgLogic.getUnstoredMatchIds(storedRecentMatchId)
    print(matchIds)
    for matchId in matchIds:
        print("matchid under")
        #PubgLogic.printJson(matchId)
        print("matchid above")
        storeMatch(str(matchId))

def storeMatch(matchId):
    PubgLogic.setMatchId(matchId)
    jsonMatchStats = PubgLogic.getMatchStats(matchId)
    PubgLogic.printJson(jsonMatchStats)
    jsonMatchStats = PubgLogic.getPlayerMatchStats(jsonMatchStats)
    PubgLogic.storePMSintoPMS(jsonMatchStats)
    pms = PubgLogic.getPms()
    SheetsLogic.appendPms(pms)
