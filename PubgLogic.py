import requests
import json
import io
import PlayerStats

class PubgLogic:
    def __init__(s):
        s.ps = PlayerStats.PlayerStats()
        with open('userInput.json', 'r') as userInputFile:
            userInput = json.load(userInputFile)
            s.player1 = userInput["player1"]
            s.player2 = userInput["player2"]
            s.bUrl = 'https://api.pubg.com/shards/pc-' + userInput["region"] + '/'
            s.headers = {'Authorization':'Bearer ' + userInput["pubgApiKey"], 'Accept':'application/vnd.api+json'}

    def getPlayerRecentMatchStat(s):
        s.ps.storeMatchStats(s.getPlayerMatchStats(s.getMatchStats(s.getRecentMatchId(s.getPlayerInfo(s.player1)))))

    def getPlayerInfo(s):
        rUrl = 'players?filter[playerNames]=' + s.player1
        s.jsonPlayerInfo = json.load(io.StringIO(requests.get(s.bUrl + rUrl, headers=s.headers).text))
        s.pId = s.jsonPlayerInfo["data"][0]["id"]
        return s.jsonPlayerInfo

    def getMatchHistory(s):
        s.jsonMatchHistory = s.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]
        return s.jsonMatchHistory

    def getRecentMatchId(s):
        s.matchId = s.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
        return s.matchId

    def getUnstoredMatchIds(s, recentMatchId):
        s.matchIds = []
        for jsonPlayerInfo in s.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]:
            if recentMatchId == jsonPlayerInfo["id"]:
                print("HELLO THERE" + len(s.matchIds))
                return s.matchIds
            else:
                s.matchIds.append(jsonPlayerInfo["id"])
        return s.matchIds

    def getMatchStats(s, matchId):
        rUrl = 'matches/' + matchId
        return json.load(io.StringIO(requests.get(s.bUrl + rUrl, headers=s.headers).text))

    def getPlayerMatchStats(s, jsonMatchStats):
        for jsonMatchStatsIncluded in jsonMatchStats["included"]:
            try:
                if jsonMatchStatsIncluded["attributes"]["stats"]["playerId"] == s.pId:
                    jsonPlayerStats = jsonMatchStatsIncluded["attributes"]["stats"]
                    # s.god.ps.storeStrObj(str(jsonPlayerStats))
                    # s.god.ps.storeJsonObj(jsonPlayerStats)
                    return jsonPlayerStats
            except KeyError:
                pass

    def printJson(s, jsonObj):
        print(json.dumps(jsonObj, indent=4, sort_keys=True))

