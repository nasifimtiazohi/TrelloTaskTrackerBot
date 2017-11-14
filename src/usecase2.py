import trellocall
import time
import db_helper

slackname_to_trelloname = []
slackname_to_trelloname = {
        'simtiaz':'sheikhnasifimtiaz',
        'gyu9':"guanxuyu",
        'xfu7':'xiaotingfu1',
        'vgupta8':'vinay638',
        'yhu22': 'otto292'}
trelloname  = slackname_to_trelloname['xfu7']
print trelloname 

#delay should be hours
def mainFlow(threadName, delay):
    dayCount = 0
    while True:
        dayCount += 1
        trellocall.getPerformancePoints()
        if dayCount == 7:
            dayCount = 0
        time.sleep(24*60*60)


db_helper.sync_card_info()