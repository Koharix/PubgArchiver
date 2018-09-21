import requests
import json
import io

class PubgLogic:
    def __init__(self, god):
        self.god = god
        self.headers = {'Authorization':'Bearer ' + god.ui.pubgApiKey, 'Accept':'application/vnd.api+json'}
        #case statement for region
        if(self.god.ui.region == 'na'):
            self.burl = 'https://api.pubg.com/shards/pc-na/'


    def getPlayerRecentMatchStat(self, player):
        self.storePMSintoPMS(self.getPlayerMatchStats(self.getMatchStats(self.getRecentMatchId(self.getPlayerInfo(player)))))

    def getPlayerInfo(self, player):
        rurl = 'players?filter[playerNames]=' + player
        jsonPlayerInfo = json.load(io.StringIO(requests.get(self.burl + rurl, headers=self.headers).text))
        self.storePlayerId(jsonPlayerInfo)
        self.storePlayerInfo(jsonPlayerInfo)
        return jsonPlayerInfo

    def getMatchHistory(self, jsonPlayerInfo):
        jsonMatchHistory = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]
        self.storeMatchHistory(jsonMatchHistory)
        return jsonMatchHistory

    def getRecentMatchId(self, jsonPlayerInfo):
        matchId = jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"][0]["id"]
        self.setMatchId(matchId)
        return matchId

    def getUnstoredMatchIds(self, storedRecentMatchId):
        array = []
        for jsonPlayerInfo in self.god.pms.jsonPlayerInfo["data"][0]["relationships"]["matches"]["data"]:
            if storedRecentMatchId == jsonPlayerInfo["id"]:
                return array
            else:
                array.append(jsonPlayerInfo["id"])

    #returns most recent match information of player
    def getMatchStats(self, matchId):
        rurl = 'matches/' + matchId
        return json.load(io.StringIO(requests.get(self.burl + rurl, headers=self.headers).text))

    def getPlayerMatchStats(self, jsonMatchStats):
        for jsonMatchStats in jsonMatchStats["included"]:
            try:
                if jsonMatchStats["attributes"]["stats"]["playerId"] == self.pms.playerId:
                    jsonPlayerStats = jsonMatchStats["attributes"]["stats"]
                    self.god.pms.storeStrObj(str(jsonPlayerStats))
                    self.god.pms.storeJsonObj(jsonPlayerStats)
                    return jsonPlayerStats
            except KeyError:
                pass

    def setMatchId(self, matchId):
        self.god.pms.setMatchId(matchId)

    def storePlayerId(self, jsonPlayerInfo):
        self.god.pms.storePlayerId(jsonPlayerInfo["data"][0]["id"])

    def storePlayerInfo(self, jsonPlayerInfo):
        self.god.pms.setPlayerInfo(jsonPlayerInfo)

    def storeMatchHistory(self, jsonMatchHistory):
        self.god.pms.storeMatchHistory(self, jsonMatchHistory)

    def storePMSintoPMS(self, jsonPlayerStats):
        self.god.pms.storeMatchStats(jsonPlayerStats)

    def printJson(self, jsonObj):
        print(json.dumps(jsonObj, indent=4, sort_keys=True))

