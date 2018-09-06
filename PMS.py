import json

#Player Match Stats
class PMS:
    def __init__(self):
        pass
    def storePlayerId(self, playerId):
        self.playerId = playerId
    def storeMatchId(self, matchId):
        self.matchId = matchId
    def storeStrObj(self, strPms):
        self.strPms = strPms
    def storeJsonObj(self, jsonObj):
        self.jsonPMS = jsonObj
    def storeMatchStats(self, playerStats):
        self.array = [str(playerStats["DBNOs"]),
        str(playerStats["assists"]),
        str(playerStats["boosts"]),
        str(playerStats["damageDealt"]),
        playerStats["deathType"],
        str(playerStats["headshotKills"]),
        str(playerStats["heals"]),
        str(playerStats["killPlace"]),
        str(playerStats["killPoints"]),
        str(playerStats["killPointsDelta"]),
        str(playerStats["killStreaks"]),
        str(playerStats["kills"]),
        str(playerStats["lastKillPoints"]),
        str(playerStats["lastWinPoints"]),
        str(playerStats["longestKill"]),
        str(playerStats["mostDamage"]),
        playerStats["name"],
        playerStats["playerId"],
        str(playerStats["revives"]),
        str(playerStats["rideDistance"]),
        str(playerStats["roadKills"]),
        str(playerStats["swimDistance"]),
        str(playerStats["teamKills"]),
        str(playerStats["timeSurvived"]),
        str(playerStats["vehicleDestroys"]),
        str(playerStats["walkDistance"]),
        str(playerStats["weaponsAcquired"]),
        str(playerStats["winPlace"]),
        str(playerStats["winPoints"]),
        str(playerStats["winPointsDelta"]),
        self.matchId]
