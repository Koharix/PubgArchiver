import SheetsLogic
import PlayerStats

ps = PlayerStats.PlayerStats()
sl = SheetsLogic.SheetsLogic(ps)
print(sl.get_recent_match_id())
sl.set_recent_match_id('hellothere2')