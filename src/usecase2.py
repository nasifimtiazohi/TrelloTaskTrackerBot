import trellocall
import time
import db_helper
import datetime

# slackname_to_trelloname = []
# slackname_to_trelloname = {
#         'simtiaz':'sheikhnasifimtiaz',
#         'gyu9':"guanxuyu",
#         'xfu7':'xiaotingfu1',
#         'vgupta8':'vinay638',
#         'yhu22': 'otto292'}
# trelloname  = slackname_to_trelloname['xfu7']

#delay should be hours
def mainFlow(threadName, delay):
    dayCount = 0
    members_dict = trellocall.members_dict
    trellocall.initPerformancePoint()
    trellocall.updateTargets(24*7) # seven days
    while True:
        dayCount += 1
        trellocall.getPerformancePoints(24) # get performance every day
        currentUTCtime = datetime.datetime.utcnow()
        if currentUTCtime.weekday() == 0:
            trellocall.updateTargets(24*7)
            trellocall.initPerformancePoint()
        time.sleep(24*60*60) # sleep one day

db_helper.sync_card_info()
