import PubgLogic
import SheetsLogic
import CombinedLogic

player = 'Koharix'
# #pms = PubgLogic.getPlayerRecentMatchStat(player)
# #SheetsLogic.setRecentMatchId(pms)
# # pms = PubgLogic.getPlayerRecentMatchStat('Koharix')
# # SheetsLogic.appendPms(pms)
# # print(SheetsLogic.getMostRecentMatchId())
# PubgLogic.printJson(PubgLogic.getMatchHistory(PubgLogic.getPlayerInfo(player)))
# recentStoredMatchId = SheetsLogic.getRecentMatchId()
# array = PubgLogic.getUnstoredMatchIds(recentStoredMatchId)
# print(array)
CombinedLogic.storeRecentMatchs(player)