from utils import Sheets, Stats

ps = Stats.PlayerStats()
sl = Sheets.SheetsLogic(ps)
print(sl.get_recent_match_id())
sl.set_recent_match_id('hellothere2')