

class PMS:
    # DBNO
    # assists
    # boosts
    # damgeDealt
    # deatType
    # headshotKills
    # heals
    # killPlace
    # killPoints
    # killPointsDelta
    # killStreaks
    # kills
    # lastKillPoints
    # lastWinPoints
    # longestKill
    # mostDamage
    # name
    # playerId
    # revives
    # rideDistance
    # roadKills
    # swimDistance
    # teamKills
    # timeSurvived
    # vehicleDestroys
    # walkDistance
    # weaponsAcquired
    # winPlace
    # winPoints
    # winPointsDelta
    def __init__(self, playerStats):
        self.DBNOs = playerStats["DBNOs"]
        self.assists = playerStats["assists"]
        self.boosts = playerStats["boosts"]
        self.damageDealt = playerStats["damageDealt"]
        self.deathType = playerStats["deathType"]
        self.headshotKills = playerStats["headshotKills"]
        self.heals = playerStats["heals"]
        self.killPlace = playerStats["killPlace"]
        self.killPoints = playerStats["killPoints"]
        self.killPointsDelta = playerStats["killPointsDelta"]
        self.killStreaks = playerStats["killStreaks"]
        self.kills = playerStats["kills"]
        self.lastKillPoints = playerStats["lastKillPoints"]
        self.lastWinPoints = playerStats["lastWinPoints"]
        self.longestKill = playerStats["longestKill"]
        self.mostDamage = playerStats["mostDamage"]
        self.name = playerStats["name"]
        self.playerId = playerStats["playerId"]
        self.revives = playerStats["revives"]
        self.rideDistance = playerStats["rideDistance"]
        self.roadKills = playerStats["roadKills"]
        self.swimDistance = playerStats["swimDistance"]
        self.teamKills = playerStats["teamKills"]
        self.timeSurvived = playerStats["timeSurvived"]
        self.vehicleDestroys = playerStats["vehicleDestroys"]
        self.walkDistance = playerStats["walkDistance"]
        self.weaponsAcquired = playerStats["weaponsAcquired"]
        self.winPlace = playerStats["winPlace"]
        self.winPoints = playerStats["winPoints"]
        self.winPointsDelta = playerStats["winPointsDelta"]