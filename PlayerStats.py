import json

#Player Match Stats
class PlayerStats:
    def __init__(s):
        pass

    def storePlayerId(s, pId):
        s.pId = pId

    def setPlayerInfo(s, jsonPlayerInfo):
        s.jsonPlayerInfo = jsonPlayerInfo

    def storeMatchHistory(s, jsonMatchHistory):
        s.jsonMatchHistory = jsonMatchHistory

    def setMatchId(s, matchId):
        s.matchId = matchId

    def storeStrObj(s, strPms):
        s.strPms = strPms

    def storeJsonObj(s, jsonObj):
        s.jsonPMS = jsonObj

    def storeMatchStats(s, playerStats):
        s.array = [str(playerStats["DBNOs"]),
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
        s.matchId]
