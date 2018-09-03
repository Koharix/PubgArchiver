import requests
import json
import io
import PMS

#google sheets
#ClientId = '450833891653-adbtqcc41jeovp2sg75gfqckc1k1s8ij.apps.googleusercontent.com'
#ClientId = ' 450833891653-adbtqcc41jeovp2sg75gfqckc1k1s8ij.apps.googleusercontent.com S'
#CilentSecret = ' r6LDwPRUe0ISwAMDPT2tQimJ '

apiKey = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiNjEwODgyMC04ZjZhLTAxMzYtM2JkMi0xN2NlYWJkMDhhYTkiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTM1NzMzNzIyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImtvaGFyaXgtZGF0YSJ9.dGsB2H8IVJjQTc8x5vL4BTTIdffe9rj3ld3DUUTlvhg '
headers = {'Authorization':'Bearer ' + apiKey, 'Accept':'application/vnd.api+json'}
burl = 'https://api.pubg.com/shards/pc-na/'
pms = PMS.PMS()

def getPlayerRecentMatchStat(player):
    storePMSintoPMS(getPlayerMatchStats(getMatchStats(getRecentMatchId(getPlayerInfo(player)))))
    return pms

def storePlayerId(jsonPlayerInfo):
    pms.storePlayerId(jsonPlayerInfo["data"][0]["id"])
    print(pms.playerId)

def getPlayerInfo(player):
    rurl = 'players?filter[playerNames]=' + player
    jsonPlayerInfo = json.load(io.StringIO(requests.get(burl + rurl, headers=headers).text))
    storePlayerId(jsonPlayerInfo)
    return jsonPlayerInfo

def getRecentMatchId(jsonPlayerInfo):
    return jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]

#returns most recent match information of player
def getMatchStats(matchId):
    rurl = 'matches/' + matchId
    return json.load(io.StringIO(requests.get(burl + rurl, headers=headers).text))

def getPlayerMatchStats(jsonMatchStats):
    for jsonMatchStats in jsonMatchStats["included"]:
        try:
            if jsonMatchStats["attributes"]["stats"]["playerId"] == pms.playerId:
                jsonPlayerStats = jsonMatchStats["attributes"]["stats"] #possible in future to remove playerStats
                #print(json.dumps(matchStats["attributes"]["stats"], indent=4, sort_keys=True))
                #print('')
                return jsonPlayerStats
        except KeyError:
            pass

def storePMSintoPMS(jsonPlayerStats):
    pms.storeMatchStats(jsonPlayerStats)