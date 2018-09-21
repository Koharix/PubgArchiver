import requests
import json
import io

class PubgLogic:
    def __init__(self, god):
        self.god = god
        self.headers = {'Authorization':'Bearer ' + self.god.ui.pubgApiKey, 'Accept':'application/vnd.api+json'}
        #case statement for region
        if(self.god.ui.region == 'na'):
            self.burl = 'https://api.pubg.com/shards/pc-na/'


    def getPlayerRecentMatchStat(self):
        self.storePMSintoPMS(self.getPlayerMatchStats(self.getMatchStats(self.getRecentMatchId(self.getPlayerInfo(self.god.ui.player1)))))

    def getPlayerInfo(self):
        rurl = 'players?filter[playerNames]=' + self.god.ui.player1
        jsonPlayerInfo = json.load(io.StringIO(requests.get(self.burl + rurl, headers=self.headers).text))
        self.storePlayerId(jsonPlayerInfo)
        self.storePlayerInfo(jsonPlayerInfo)
        return jsonPlayerInfo

    def getMatchHistory(self, jsonPlayerInfo):
        jsonMatchHistory = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]
        self.storeMatchHistory(jsonMatchHistory)
        return jsonMatchHistory

    def getRecentMatchId(self, jsonPlayerInfo):
        self.matchId = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
        self.setMatchId(self.matchId)
        return self.matchId

    def getUnstoredMatchIds(self):
        self.matchIds = []
        for jsonPlayerInfo in self.god.ps.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]:
            if self.god.sl.recentMatchId == jsonPlayerInfo["id"]:
                return self.matchIds
            else:
                self.matchIds.append(jsonPlayerInfo["id"])

    #returns most recent match information of player
    def getMatchStats(self, matchId):
        rurl = 'matches/' + matchId
        return json.load(io.StringIO(requests.get(self.burl + rurl, headers=self.headers).text))

    def getPlayerMatchStats(self, jsonMatchStats):
        for jsonMatchStats in jsonMatchStats["included"]:
            try:
                if jsonMatchStats["attributes"]["stats"]["playerId"] == self.god.ps.playerId:
                    jsonPlayerStats = jsonMatchStats["attributes"]["stats"]
                    self.god.ps.storeStrObj(str(jsonPlayerStats))
                    self.god.ps.storeJsonObj(jsonPlayerStats)
                    return jsonPlayerStats
            except KeyError:
                pass

    def setMatchId(self, matchId):
        self.god.ps.matchId = matchId

    def storePlayerId(self, jsonPlayerInfo):
        self.god.ps.playerId = jsonPlayerInfo["data"][0]["id"]

    def storePlayerInfo(self, jsonPlayerInfo):
        self.god.ps.jsonPlayerInfo = jsonPlayerInfo

    def storeMatchHistory(self, jsonMatchHistory):
        self.god.ps.jsonMatchHistory = jsonMatchHistory

    def storePMSintoPMS(self, jsonPlayerStats):
        self.god.ps.storeMatchStats(jsonPlayerStats)

    def printJson(self, jsonObj):
        print(json.dumps(jsonObj, indent=4, sort_keys=True))

