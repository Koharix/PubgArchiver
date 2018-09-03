import Logic
import json

player = 'Koharix'
pms = Logic.getPlayerRecentMatchStat(player)
print(pms.winPlace)
