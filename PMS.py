
#Player Match Stats
class PMS:
    def __init__(self):
        asdf = 0
    def storePlayerId(self, playerId):
        self.playerId = playerId
    def storeMatchStats(self, playerStats):
        self.DBNOs = str(playerStats["DBNOs"])
        self.assists = str(playerStats["assists"])
        self.boosts = str(playerStats["boosts"])
        self.damageDealt = str(playerStats["damageDealt"])
        self.deathType = playerStats["deathType"]
        self.headshotKills = str(playerStats["headshotKills"])
        self.heals = str(playerStats["heals"])
        self.killPlace = str(playerStats["killPlace"])
        self.killPoints = str(playerStats["killPoints"])
        self.killPointsDelta = str(playerStats["killPointsDelta"])
        self.killStreaks = str(playerStats["killStreaks"])
        self.kills = str(playerStats["kills"])
        self.lastKillPoints = str(playerStats["lastKillPoints"])
        self.lastWinPoints = str(playerStats["lastWinPoints"])
        self.longestKill = str(playerStats["longestKill"])
        self.mostDamage = str(playerStats["mostDamage"])
        self.name = playerStats["name"]
        self.playerId = playerStats["playerId"]
        self.revives = str(playerStats["revives"])
        self.rideDistance = str(playerStats["rideDistance"])
        self.roadKills = str(playerStats["roadKills"])
        self.swimDistance = str(playerStats["swimDistance"])
        self.teamKills = str(playerStats["teamKills"])
        self.timeSurvived = str(playerStats["timeSurvived"])
        self.vehicleDestroys = str(playerStats["vehicleDestroys"])
        self.walkDistance = str(playerStats["walkDistance"])
        self.weaponsAcquired = str(playerStats["weaponsAcquired"])
        self.winPlace = str(playerStats["winPlace"])
        self.winPoints = str(playerStats["winPoints"])
        self.winPointsDelta = str(playerStats["winPointsDelta"])