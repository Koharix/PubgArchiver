import requests
import json
import io
import PlayerStats


class PubgLogic:

    def __init__(self):
        self.ps = PlayerStats.PlayerStats()
        with open('userInput.json', 'r') as userInputFile:
            userInput = json.load(userInputFile)
            self.player1 = userInput["player1"]
            self.player2 = userInput["player2"]
            self.baseUrl = 'https://api.pubg.com/shards/pc-' + userInput["region"] + '/'
            self.headers = {'Authorization':'Bearer ' + userInput["pubgApiKey"], 'Accept':'application/vnd.api+json'}

    def get_player_info(self):
        relativeUrl = 'players?filter[playerNames]=' + self.player1
        self.jsonPlayerInfo = json.load(io.StringIO(requests.get(self.baseUrl + relativeUrl, headers=self.headers).text))
        self.playerId = self.jsonPlayerInfo["data"][0]["id"]
        return self.jsonPlayerInfo

    def get_match_history(self):
        self.jsonMatchHistory = self.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]
        return self.jsonMatchHistory

    def get_recent_matchId(self):
        self.matchId = self.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
        return self.matchId

    def get_unstored_match_ids(self, recentMatchId):
        self.matchIds = []
        for jsonPlayerInfo in self.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]:
            if recentMatchId == jsonPlayerInfo["id"]:
                print("HELLO THERE" + len(self.matchIds))
                return self.matchIds
            else:
                self.matchIds.append(jsonPlayerInfo["id"])
        return self.matchIds

    def get_match_stats(self, matchId):
        relativeUrl = 'matches/' + matchId
        return json.load(io.StringIO(requests.get(self.baseUrl + relativeUrl, headers=self.headers).text))

    def get_player_match_stats(self, jsonMatchStats):
        for jsonMatchStatsIncluded in jsonMatchStats["included"]:
            try:
                if jsonMatchStatsIncluded["attributes"]["stats"]["playerId"] == self.playerId:
                    jsonPlayerStats = jsonMatchStatsIncluded["attributes"]["stats"]
                    return jsonPlayerStats
            except KeyError:
                pass

    def print_json(self, jsonObj):
        print(json.dumps(jsonObj, indent=4, sort_keys=True))

