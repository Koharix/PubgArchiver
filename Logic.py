import requests
import json
import io
import PMS

apiKey = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiNjEwODgyMC04ZjZhLTAxMzYtM2JkMi0xN2NlYWJkMDhhYTkiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTM1NzMzNzIyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImtvaGFyaXgtZGF0YSJ9.dGsB2H8IVJjQTc8x5vL4BTTIdffe9rj3ld3DUUTlvhg '
headers = {'Authorization':'Bearer '+apiKey, 'Accept':'application/vnd.api+json'}
burl = 'https://api.pubg.com/shards/pc-na/'
KId = 'account.c4e1432d27bd4d9296b7ad058c49172a'
MId = 'account.c8335a1816ee452ea757695d0b811259'

def getPlayerInfo(player):
    rurl = 'players?filter[playerNames]=' + player
    r = requests.get(burl + rurl, headers=headers)
    #print(r)
    #print(r.text)
    return r

def getMatchId(player):
    data = getPlayerInfo(player).text
    data = json.load(io.StringIO((data)))
    matchId = data["data"][0]["relationships"]["matches"]["data"][0]["id"]
    print(matchId)
    return matchId

#returns most recent match information of player
def getMatchStat(player):
    matchId = getMatchId(player)
    rurl = 'matches/' + matchId
    r = requests.get(burl + rurl, headers=headers)
    print(r)
    #print(r.text)
    return r

def getPlayerMatchStats(player):
    matchStats = json.load(io.StringIO((getMatchStat(player).text)))
    matchStats = matchStats["included"]
    for x in matchStats:
        try:
            if x["attributes"]["stats"]["playerId"] == KId:
                playerStats = x["attributes"]["stats"]
                print(playerStats)
                print(json.dumps(playerStats, indent=4, sort_keys=True))

                return playerStats
        except KeyError:
            doNothing = 0

def storePMSintoPMS(player):
    playerstats = getPlayerMatchStats(player)
    pms = PMS.PMS(playerstats)
