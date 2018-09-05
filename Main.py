import PubgLogic
import json
import SheetsLogic

player = 'Koharix'
pms = PubgLogic.getPlayerRecentMatchStat('Koharix')
SheetsLogic.storePms(pms)
