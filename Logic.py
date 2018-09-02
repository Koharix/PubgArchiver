import requests
import json
import io
import PMS

apiKey = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiNjEwODgyMC04ZjZhLTAxMzYtM2JkMi0xN2NlYWJkMDhhYTkiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTM1NzMzNzIyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImtvaGFyaXgtZGF0YSJ9.dGsB2H8IVJjQTc8x5vL4BTTIdffe9rj3ld3DUUTlvhg '
headers = {'Authorization':'Bearer '+apiKey, 'Accept':'application/vnd.api+json'}
burl = 'https://api.pubg.com/shards/pc-na/'
KId = 'account.c4e1432d27bd4d9296b7ad058c49172a'
MId = 'account.c8335a1816ee452ea757695d0b811259'
pms = PMS.PMS()

def storePlayerId(playerInfo):
    pms.storePlayerId(playerInfo["data"][0]["id"])

def getPlayerInfo(player):
    rurl = 'players?filter[playerNames]=' + player
    playerInfo = json.load(io.StringIO((requests.get(burl + rurl, headers=headers)).text))
    storePlayerId(playerInfo)
    return playerInfo

def getMatchId(player):
    playerInfo = (getPlayerInfo(player))
    matchId = playerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
    return matchId

#returns most recent match information of player
def getMatchStat(player):
    matchId = getMatchId(player)
    rurl = 'matches/' + matchId
    return json.load(io.StringIO((requests.get(burl + rurl, headers=headers).text)))

def getPlayerMatchStats(player):
    matchStats = getMatchStat(player)["included"]
    for matchStats in matchStats:
        try:
            if matchStats["attributes"]["stats"]["playerId"] == pms.playerId:
                playerStats = matchStats["attributes"]["stats"]
                print(json.dumps(playerStats, indent=4, sort_keys=True))
                print('')
                return playerStats
        except KeyError:
            doNothing = 0

def storePMSintoPMS(player):
    playerstats = getPlayerMatchStats(player)
    pms.storeMatchStats(playerstats)
    return pms
