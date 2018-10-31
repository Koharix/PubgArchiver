import SheetsLogic
import PlayerStats

ps = PlayerStats.PlayerStats()
sl = SheetsLogic.SheetsLogic(ps)
print(sl.getRecentMatchId())
sl.setRecentMatchId('hellothere2')