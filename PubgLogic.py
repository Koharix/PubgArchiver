import requests
import json
import io
import PMS

apiKey = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiNjEwODgyMC04ZjZhLTAxMzYtM2JkMi0xN2NlYWJkMDhhYTkiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTM1NzMzNzIyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImtvaGFyaXgtZGF0YSJ9.dGsB2H8IVJjQTc8x5vL4BTTIdffe9rj3ld3DUUTlvhg '
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
    return jsonPlayerInfo

def getMatchHistory(jsonPlayerInfo):
    jsonMatchHistory = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]
    storeMatchHistory(jsonMatchHistory)
    return jsonMatchHistory

def getRecentMatchId(jsonPlayerInfo):
    matchId = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
    setMatchId(matchId)
    return matchId

def getUnstoredMatchIds(recentStoredMatchId):
    array = []
    for jsonMatchHistory in pms.jsonMatchHistory:
        if recentStoredMatchId == jsonMatchHistory["id"]:
            return array
        else:
            array.append(recentStoredMatchId)

def setMatchId(matchId):
    pms.setMatchId(matchId)

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

def storePlayerId(jsonPlayerInfo):
    pms.storePlayerId(jsonPlayerInfo["data"][0]["id"])

def storeMatchHistory(jsonMatchHistory):
    pms.storeMatchHistory(jsonMatchHistory)

def storePMSintoPMS(jsonPlayerStats):
    pms.storeMatchStats(jsonPlayerStats)

def printJson(jsonObj):
    print(json.dumps(jsonObj, indent=4, sort_keys=True))
