import PubgLogic
import SheetsLogic
import userInput

ui = userInput.userInput(userInput.json)
def storeRecentMatchs(player):
    PubgLogic.getPlayerInfo(player)
    storedRecentMatchId = SheetsLogic.getRecentMatchId()
    matchIds = PubgLogic.getUnstoredMatchIds(storedRecentMatchId)
    for matchId in matchIds:
        storeMatch(str(matchId))

def storeMatch(matchId):
    PubgLogic.setMatchId(matchId)
    jsonMatchStats = PubgLogic.getMatchStats(matchId)
    jsonMatchStats = PubgLogic.getPlayerMatchStats(jsonMatchStats)
    PubgLogic.storePMSintoPMS(jsonMatchStats)
    pms = PubgLogic.getPms()
    SheetsLogic.appendPms(pms)


