import SheetsLogic
import PlayerStats
import PubgLogic


class CombinedLogic:

    def __init__(self):
        self.ps = PlayerStats.PlayerStats()
        self.pl = PubgLogic.PubgLogic()
        self.sl = SheetsLogic.SheetsLogic(self.ps)

    def store_recent_matchs(self):
        self.pl.get_player_info()
        storedRecentMatchId = self.sl.get_recent_matchId()
        matchIds = self.pl.get_unstored_match_ids(storedRecentMatchId)
        if (matchIds > 0):
            self.sl.set_recent_match_id(matchIds[0])
            print("HELLO THERE" + str(len(matchIds)))
            for matchId in matchIds:
                self.store_match(str(matchId))

    def store_match(self, matchId):
        self.ps.set_match_id(matchId)
        jsonMatchStats = self.pl.get_match_stats(matchId)
        jsonPlayerStats = self.pl.get_player_match_stats(jsonMatchStats)
        self.ps.store_match_stats(jsonPlayerStats)
        self.sl.append_pms(matchId, self.ps.array)


