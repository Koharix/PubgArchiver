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
            s.baseUrl = 'https://api.pubg.com/shards/pc-' + userInput["region"] + '/'
            s.headers = {'Authorization':'Bearer ' + userInput["pubgApiKey"], 'Accept':'application/vnd.api+json'}

    def getPlayerRecentMatchStat(s):
        s.ps.storeMatchStats(s.getPlayerMatchStats(s.getMatchStats(s.getRecentMatchId(PubgLogic.getPlayerInfo(s.player1)))))

    def getPlayerInfo(s):
        relativeUrl = 'players?filter[playerNames]=' + s.player1
        s.jsonPlayerInfo = json.load(io.StringIO(requests.get(s.baseUrl + relativeUrl, headers=s.headers).text))
        s.playerId = s.jsonPlayerInfo["data"][0]["id"]
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
        relativeUrl = 'matches/' + matchId
        return json.load(io.StringIO(requests.get(s.baseUrl + relativeUrl, headers=s.headers).text))

    def getPlayerMatchStats(s, jsonMatchStats):
        for jsonMatchStatsIncluded in jsonMatchStats["included"]:
            try:
                if jsonMatchStatsIncluded["attributes"]["stats"]["playerId"] == s.playerId:
                    jsonPlayerStats = jsonMatchStatsIncluded["attributes"]["stats"]
                    return jsonPlayerStats
            except KeyError:
                pass

    def printJson(s, jsonObj):
        print(json.dumps(jsonObj, indent=4, sort_keys=True))

