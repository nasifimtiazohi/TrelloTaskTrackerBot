import trellocall
import time
import db_helper

#delay should be hours
def mainFlow(threadName, delay):
    dayCount = 0
    while True:
        dayCount += 1
        trellocall.getPerformancePoints()
        if dayCount == 7:
            dayCount = 0
        time.sleep(24*60*60)
        


