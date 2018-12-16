

class PlayerStats:
    def __init__(self):
        self.p_id = None                # player id
        self.matchId = None             # match id
        self.matchStats = None          # Map of a players stats for a match
        pass

    def store_player_id(self, uid):
        self.p_id = uid

    def set_match_id(self, match_id):
        self.matchId = match_id

    def store_match_stats(self, player_stats):
        self.matchStats = {
            "DBNOs": str(player_stats["DBNOs"]),
            "assists": str(player_stats["assists"]),
            "boosts": str(player_stats["boosts"]),
            "damageDealt": str(player_stats["damageDealt"]),
            "deathType": player_stats["deathType"],
            "headshotKills": str(player_stats["headshotKills"]),
            "heals": str(player_stats["heals"]),
            "killPlace": str(player_stats["killPlace"]),
            "killPoints": str(player_stats["killPoints"]),
            "killPointsDelta": str(player_stats["killPointsDelta"]),
            "killStreaks": str(player_stats["killStreaks"]),
            "kills": str(player_stats["kills"]),
            "lastKillPoints": str(player_stats["lastKillPoints"]),
            "lastWinPoints": str(player_stats["lastWinPoints"]),
            "longestKill": str(player_stats["longestKill"]),
            "mostDamage": str(player_stats["mostDamage"]),
            "name": player_stats["name"],
            "playerId": player_stats["playerId"],
            "revives": str(player_stats["revives"]),
            "rideDistance": str(player_stats["rideDistance"]),
            "roadKills": str(player_stats["roadKills"]),
            "swimDistance": str(player_stats["swimDistance"]),
            "teamKills": str(player_stats["teamKills"]),
            "timeSurvived": str(player_stats["timeSurvived"]),
            "vehicleDestroys": str(player_stats["vehicleDestroys"]),
            "walkDistance": str(player_stats["walkDistance"]),
            "weaponsAcquired": str(player_stats["weaponsAcquired"]),
            "winPlace": str(player_stats["winPlace"]),
            "winPoints": str(player_stats["winPoints"]),
            "winPointsDelta": str(player_stats["winPointsDelta"]),
            "matchId": self.matchId
        }
