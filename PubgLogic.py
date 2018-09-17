import requests
import json
import io
import PMS


with open('pubgApiKey.txt', 'r') as myfile:
    apiKey=myfile.read()

headers = {'Authorization':'Bearer ' + apiKey, 'Accept':'application/vnd.api+json'}
burl = 'https://api.pubg.com/shards/pc-na/'
pms = PMS.PMS()

def getPlayerRecentMatchStat(player):
    storePMSintoPMS(getPlayerMatchStats(getMatchStats(getRecentMatchId(getPlayerInfo(player)))))
    return pms

def getPlayerInfo(player):
    rurl = 'players?filter[playerNames]=' + player
    jsonPlayerInfo = json.load(io.StringIO(requests.get(burl + rurl, headers=headers).text))
    storePlayerId(jsonPlayerInfo)
    storePlayerInfo(jsonPlayerInfo)
    return jsonPlayerInfo

def getMatchHistory(jsonPlayerInfo):
    jsonMatchHistory = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]
    storeMatchHistory(jsonMatchHistory)
    return jsonMatchHistory

def getRecentMatchId(jsonPlayerInfo):
    matchId = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
    setMatchId(matchId)
    return matchId

def getUnstoredMatchIds(storedRecentMatchId):
    array = []
    for jsonPlayerInfo in pms.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]:
        if storedRecentMatchId == jsonPlayerInfo["id"]:
            return array
        else:
            array.append(jsonPlayerInfo["id"])

#returns most recent match information of player
def getMatchStats(matchId):
    rurl = 'matches/' + matchId
    return json.load(io.StringIO(requests.get(burl + rurl, headers=headers).text))

def getPlayerMatchStats(jsonMatchStats):
    for jsonMatchStats in jsonMatchStats["included"]:
        try:
            if jsonMatchStats["attributes"]["stats"]["playerId"] == pms.playerId:
                jsonPlayerStats = jsonMatchStats["attributes"]["stats"]
                pms.storeStrObj(str(jsonPlayerStats))
                pms.storeJsonObj(jsonPlayerStats)
                return jsonPlayerStats
        except KeyError:
            pass

def getPms():
    return pms

def setMatchId(matchId):
    pms.setMatchId(matchId)

def storePlayerId(jsonPlayerInfo):
    pms.storePlayerId(jsonPlayerInfo["data"][0]["id"])

def storePlayerInfo(jsonPlayerInfo):
    pms.setPlayerInfo(jsonPlayerInfo)

def storeMatchHistory(jsonMatchHistory):
    pms.storeMatchHistory(jsonMatchHistory)

def storePMSintoPMS(jsonPlayerStats):
    pms.storeMatchStats(jsonPlayerStats)

def printJson(jsonObj):
    print(json.dumps(jsonObj, indent=4, sort_keys=True))


