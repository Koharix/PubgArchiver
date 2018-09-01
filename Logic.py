import requests
import json
import io

apiKey = 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiJiNjEwODgyMC04ZjZhLTAxMzYtM2JkMi0xN2NlYWJkMDhhYTkiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNTM1NzMzNzIyLCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6ImtvaGFyaXgtZGF0YSJ9.dGsB2H8IVJjQTc8x5vL4BTTIdffe9rj3ld3DUUTlvhg '
headers = {'Authorization':'Bearer '+apiKey, 'Accept':'application/vnd.api+json'}
burl = 'https://api.pubg.com/shards/pc-na/'
KId = 'account.c4e1432d27bd4d9296b7ad058c49172a'
MId = 'account.c8335a1816ee452ea757695d0b811259'

def searchPlayer(player):
    rurl = 'players?filter[playerNames]=' + player
    r = requests.get(burl+rurl,headers=headers)
    print(r)
    print(r.text)
    return r.text

def getMatchId(player):
    data = searchPlayer(player)
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
    print(r.text)
    return r


