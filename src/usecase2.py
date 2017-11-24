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

#delay should be hours
def mainFlow(threadName, delay):
    dayCount = 0
    members_dict = trellocall.members_dict
    while True:
        dayCount += 1
        trellocall.getPerformancePoints(24)
        trellocall.updateTargets(24)
        if dayCount == 7:
            currentTargets = trellocall.getAllTargets()
            prevTotalPoints = trellocall.getPrevTotalPoint()
            '''targetPoints = {}
            for memberID in members_dict.keys():
                targetPoints[members_dict[memberID]] = currentTargets[members_dict[memberID]] + prevTotalPoints[members_dict[memberID]]/10
            db_helper.store_target_points(targetPoints)'''
            trellocall.updateTargets(24)
            dayCount = 0
        time.sleep(24*60*60)


db_helper.sync_card_info()