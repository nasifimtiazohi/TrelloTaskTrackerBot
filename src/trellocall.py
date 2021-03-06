from trello import TrelloClient
from trello import label as trelloLabel
from difflib import SequenceMatcher
import db_helper
import struct
import datetime
import os
import pytz
import slackapicall
import json
import emailing
from db_helper import add_card, get_user_points, store_total_points, get_progress_of_card, get_user_points, get_user_target_points, store_target_points
from datetime import datetime as dt
members_dict=None
project_team=None
testboard=None

# Set up Trello environment variables, if failed here, please see the README.md
trelloKey = os.environ.get("TRELLO_API_KEY")
trelloSecret = os.environ.get("TRELLO_API_SECRET")
trelloToken = os.environ.get("TRELLO_TOKEN")
TeamName= os.environ.get("TEAM_NAME")
print TeamName
BoardName=os.environ.get("BOARD_NAME")

#TODO: Usecase3 only asks a person about progress. No matter how many cards are due. Later we'll refine it



client = TrelloClient(
    api_key = trelloKey,
    api_secret=trelloSecret,
    token=trelloToken,
    token_secret=None
)


def get_all_cards():
    opencards = testboard.open_cards()
    all_card_info=[]
    for c in opencards:
        card_info = []
        usernames = []
        # for userid in c.member_ids:
        #     user_name = members_dict[userid]
        # 'sheikhnasifimtiaz' is a slack name
        due_date = c.due
        card_id = c.id
        card_name = c.name
        #points = getPerformancePoints()[user_name]
        progress = getCardProgress(card_id)
        #only get the cards with progress
        if progress != '':
            card_info.append(due_date)
            card_info.append(card_name)
            card_info.append(progress)
            for userid in c.member_ids:
                user_name = members_dict[userid]
                usernames.append(user_name)
            card_info.append(usernames)
            card_info.append(card_id)
            #card_info.append(userid)
            all_card_info.append(card_info)
    return all_card_info

def get_all_cards_of_user(trello_username):
    opencards = testboard.open_cards()
    all_cards=[]
    for c in opencards:
        card_info = []
        for userid in c.member_ids:
            user_name = members_dict[userid]
            # 'sheikhnasifimtiaz' is a slack name
            if user_name == trello_username:
                all_cards.append(c)

    return all_cards

def get_all_cards_with_duedate():
    current_time=datetime.datetime.now()
    current_time=current_time.replace(tzinfo=pytz.utc)
    opencards=testboard.open_cards()
    duecards=[]
    for c in opencards:
        temp=c.due_date
        if c.due_date:
            temp=temp.replace(tzinfo=pytz.utc)
            temp-=datetime.timedelta(hours=5)
            if current_time<temp:
                duecards.append(c)
    ''' only sending the names for now.
    In future, we'll send info about each card '''
    namelist_with_duecards={}
    for c in duecards:
        mid=c.member_id[0]
        name=members_dict[mid]
        if name not in namelist_with_duecards.keys():
            l=[]
            l.append(c)
            namelist_with_duecards[name]=l
        else:
            namelist_with_duecards[name].append(c)
    return namelist_with_duecards



def get_all_cards_with_duetime(timeinhours):
    current_time=datetime.datetime.now()
    current_time=current_time.replace(tzinfo=pytz.utc)
    print "hello",testboard.name
    opencards=testboard.open_cards()
    duecards=[]
    for c in opencards:
        temp=c.due_date
        if c.due_date:
            colors=[]
            if c.list_labels!=None:
                for label in c.list_labels:
                    #print label.color
                    colors.append(label.color)
            temp=temp.replace(tzinfo=pytz.utc)
            temp-=datetime.timedelta(hours=5)
            temp2=temp-datetime.timedelta(hours=timeinhours)
            if current_time<temp and current_time>temp2 and 'green' not in colors:
                duecards.append(c)
    return duecards

def get_cards_for_UC1_alternate():
    opencards=testboard.open_cards()
    final=[]
    for c  in opencards:
        flag=True
        if c.list_labels:
            for label in c.list_labels:
                if  label.color=='yellow' or label.color=='sky' or label.color=='black' or label.color=='green':
                    flag=False
                    break
        if isinstance(c.due_date,str) or flag:
            print "bal" ,c.name, c.due_date, type(c.due_date), c.label_ids
            final.append(c)
    return final
def get_all_cards_for_usecase1():
    current_time=datetime.datetime.now()
    current_time=current_time.replace(tzinfo=pytz.utc)
    opencards=testboard.open_cards()
    Easy = "yellow"
    Median = "sky"
    Hard = "black"
    Finished= "green"
    HardCards=[]
    MediumCards=[]
    EasyCards=[]
    for c in opencards:
        temp=c.due_date
        if c.due_date:
            temp=temp.replace(tzinfo=pytz.utc)
            temp-=datetime.timedelta(hours=5)
            tempHard=temp-datetime.timedelta(hours=48)
            tempMedium=temp-datetime.timedelta(hours=24)
            tempEasy=temp-datetime.timedelta(hours=12)
            colors=[]
            print "heelo", c.list_labels
            if c.list_labels!=None:
                for label in c.list_labels:
                    #print label.color
                    colors.append(label.color)
            #print "colors" ,colors
            #print c.name, c.label_ids,c.due_date, current_time,tempHard,tempMedium
            if current_time<temp and current_time>tempHard and 'green' not in colors and 'black' in colors:
                #print "hard task", c.name
                HardCards.append(c)
            elif current_time<temp and current_time>tempMedium and 'green' not in colors and 'sky' in colors:
                #print "medium task", c.name
                MediumCards.append(c)
            elif current_time<temp and current_time>tempEasy and 'green' not in colors and 'yellow' in colors:
                EasyCards.append(c), c.name
    final=[EasyCards,MediumCards,HardCards]
    return final


# def print_deadline_messages():
#     message_list=[]
#     lists=testboard.all_lists()
#     for l in lists:
#         if l.name=="task within 1 day deaadline":
#             target_list=l
#             break
#     cards=target_list.list_cards()
#     members = project_team.get_members()
#     #todo: make it a dictionary for easy searching
#     for c in cards:
#         target_card=c
#         message=""
#         #todo:only search for the first member. make it about all
#         mid=target_card.member_id
#         for m in members:
#             if m.id==mid[0]:
#                 message+=m.username
#                 name=m.username
#                 break
#         message+=" is asked to complete " + c.name
#         print message
#         sendmail(name,message)
#         message_list.append(message)
#     return message_list


def members_dictionary(project_team):
    members = project_team.get_members()
    d={}
    for m in members:
        d[m.id]=m.username
    return d

def var_init():
    global project_team
    global testboard
    global members_dict
    teams=client.list_organizations()
    for t in teams:
        if t.name==TeamName:
            project_team=t
            break
    boards = project_team.get_boards(project_team)
    for b in boards:
        if b.name==BoardName:
            testboard=b
    members_dict=members_dictionary(project_team)

def trelloname_with_duetime(duetime_in_hours):
    trelloname_with_duecards=get_all_names_cards_with_duetime(duetime_in_hours)
    return trelloname_with_duecards

def slackname_with_duecards():
    trelloname_with_duecards=get_all_cards_with_duedate()
    slack=slackapicall.nameNmail()
    participants=project_team.get_members()
    d={}
    for p in participants:
        json_obj = trellocall.client.fetch_json('/members/' + p.id,query_params={'badges': False})
        d[p.username]=p.full_name.lower()
    slackname_with_duecrds={}

    for n in trelloname_with_duecards.keys():
        full_name=d[n]
        key=None
        max=0
        for k in slack.keys():
            temp=SequenceMatcher(None,k,full_name).ratio()
            if temp>max:
                max=temp
                key=k
        slackname_with_duecrds[key]=trelloname_with_duecards[n]
    return slackname_with_duecrds

def slackname_to_trelloname(slackname):
    slackname_to_trelloname_dict={}
    duecards=get_all_cards_for_usecase1()
    participants=project_team.get_members()
    d={}
    slack=slackapicall.fullnameNname()

    for p in participants:
        json_obj = client.fetch_json('/members/' + p.id,query_params={'badges': False})
        #print "dir" ,dir(p)
        d[p.full_name.lower()]=p.username
    for trelloname in d.keys():
        key=None
        max=0
        for k in slack.keys():
            temp=SequenceMatcher(None,k,trelloname).ratio()
            if temp>max:
                max=temp
                key=k
        tempname=key
        slackname_to_trelloname_dict[slack[tempname]]=d[trelloname]
    print slackname_to_trelloname_dict
    return slackname_to_trelloname_dict[slackname]

def slackname_with_duetime(duetime_in_hours):
    trelloname_with_duecards=get_all_names_cards_with_duetime(duetime_in_hours)
    slack=slackapicall.nameNmail()
    participants=project_team.get_members()
    d={}
    for p in participants:
        #print dir(p)
        json_obj = client.fetch_json('/members/' + p.id,query_params={'badges': False})
        d[p.username]=p.full_name.lower()
    slackname_with_duecrds={}

    for n in trelloname_with_duecards.keys():
        print "trello id",n
        full_name=d[n]
        key=None
        max=0
        for k in slack.keys():
            print "slack k",k
            temp=SequenceMatcher(None,k,full_name).ratio()
            if temp>max:
                max=temp
                key=k
        slackname_with_duecrds[key]=trelloname_with_duecards[n]
    return slackname_with_duecrds

def get_all_names_cards_with_duetime(timeinhours):
    current_time=datetime.datetime.now()
    current_time=current_time.replace(tzinfo=pytz.utc)
    #print "hello",testboard.name
    opencards=testboard.open_cards()
    duecards=[]
    for c in opencards:
        temp=c.due_date
        if c.due_date:
            colors=[]
            if c.list_labels!=None:
                for label in c.list_labels:
                    #print label.color
                    colors.append(label.color)
            temp=temp.replace(tzinfo=pytz.utc)
            temp-=datetime.timedelta(hours=5)
            temp2=temp-datetime.timedelta(hours=timeinhours)
            if current_time<temp and current_time>temp2 and 'green' not in colors:
                duecards.append(c)
    ''' only sending the names for now.
    In future, we'll send info about each card '''
    namelist_with_duecards={}
    for c in duecards:
        members=c.member_ids
        for mid in members:
            name=members_dict[mid]
            if name not in namelist_with_duecards.keys():
                l=[]
                l.append(c)
                namelist_with_duecards[name]=l
            else:
                namelist_with_duecards[name].append(c)
    return namelist_with_duecards

# def print_members_points():
#     curTeam=project_team
#     boards = curTeam.get_boards(curTeam)
#     members = curTeam.get_members()
#     idMembersDict = {}
#     membersPoint = {}
#     for member in members:
#         membersPoint[member.username] = 0
#     for member in members:
#         idMembersDict[member.id] = member.username
#     lists=testBoard.list_lists()
#     for list in lists:
#         if list.name == "Leader Board":
#             cards=list.list_cards()
#             #todo: make it a dictionary for easy searching
#             for card in cards:
#                 membersID = card.member_id
#                 checkLists = card.fetch_checklists()
#                 for checkList in checkLists:
#                     items = checkList.items
#                     for item in items:
#                         points = item["name"].split(' ')[0]
#                         for memberID in membersID:
#                             membersPoint[idMembersDict[memberID]] += int(points)
#     return membersPoint

def getInterval(timeInHours):
    # this is the interval for the week.
    '''today = datetime.datetime.utcnow()
    weekday = today.weekday()
    monday_delta = datetime.timedelta(weekday)
    sunday_delta = datetime.timedelta(7 - weekday)
    monday = today - monday_delta
    next_monday = today + sunday_delta
    
    monday = dt.combine(monday, dt.min.time())
    monday = monday.replace(tzinfo=pytz.utc)
    next_monday = dt.combine(next_monday, dt.min.time())
    next_monday = next_monday.replace(tzinfo=pytz.utc)'''

    # this is the interval for one day
    today = datetime.datetime.utcnow().date()
    today_begin = dt.combine(today, dt.min.time())
    today_begin = today_begin.replace(tzinfo=pytz.utc)
    today_end = today_begin + datetime.timedelta(hours = 24)
    return (today_begin, today_end)
    '''endTime = datetime.datetime.utcnow()
    endTime = endTime.replace(tzinfo=pytz.utc)
    startTime = endTime - datetime.timedelta(hours = timeInHours)'''

def getAllOpenCards():
    return testboard.open_cards()

# Completed cards
def getAllCompletedCards(cards):
    completeLable = "green"
    completeCards = []
    for card in cards:
        lables = card.list_labels
        if lables != None:
            for lable in lables:
                if lable.color == completeLable:
                    completeCards.append(card)
                    break
    return completeCards
# Incompleted cards
def getAllIncompletedCards(cards):
    inCompletedLable = "red"
    inCompletedCards = []
    for card in cards:
        lables = card.list_labels
        if lables != None :
            for lable in lables:
                if lable.color == inCompletedLable:
                    inCompletedCards.append(card)
    return inCompletedCards

def getCardProgress(card_id):
    progress = ""
    opencards=testboard.open_cards()
    inCompletedLable = "red"
    CompletedLable = "green"
    for card in opencards:
        #Go to specific card id
        if card.id == card_id:
            lables = card.list_labels
            if lables != None :
                for lable in lables:
                    if lable.color == inCompletedLable:
                        progress = "Pending"
                    if lable.color == CompletedLable:
                        progress = "Completed"
    return progress
# get all cards finished after the start time point of the current interval
def getAllCompletedCardsAtCurrentInterval(cards, interval):
    currentCompletedCards = []
    for card in cards:
        #dueDate = card.due_date
        dueDate = card.due_date.replace(tzinfo=pytz.utc)
        if dueDate > interval[0] and dueDate < interval[1]:
            currentCompletedCards.append(card)
    return currentCompletedCards

def getAllIncompletedCardsAtCurrentInterval(cards, endTimePoint):
    currentIncompleteCards = []
    for card in cards:
        dueDate = card.due_date
        '''if type(dueDate) == str:
            continue'''
        #dueDate = dueDate.replace(tzinfo=pytz.utc)
        if dueDate < endTimePoint:
            currentIncompleteCards.append(card)
    return currentIncompleteCards

def getRewardsAndBonus_of_A_Card(card_id, cards):

    points = 0
    Easy = "yellow"
    Median = "sky"
    Hard = "black"

    for card in cards :
       if card.id == card_id:
            for label in card.list_labels:
                if label.color == Easy:
                    points += 10
                    break
                if label.color == Median:
                    points += 40
                    break
                if label.color == Hard:
                    points += 50
                    break
    return points

def getRewardsAndBonus(cards):

    points = 0
    Easy = "yellow"
    Median = "sky"
    Hard = "black"

    for card in cards:
        for label in card.list_labels:
            if label.color == Easy:
                points += 10
                break
            if label.color == Median:
                points += 40
                break
            if label.color == Hard:
                points += 50
                break
    return points

def getPenalty(cards):
    penalty = 0
    Easy = "yellow"
    Median = "sky"
    Hard = "black"
    for card in cards:
        for label in card.list_labels:
            if label.color == Easy:
                penalty = penalty - 50
                break
            if label.color == Median:
                penalty = penalty - 30
                break
            if label.color == Hard:
                penalty = penalty - 10
                break
    return penalty

def getPenalty_of_A_Card(card_id, cards):
    penalty = 0
    Easy = "yellow"
    Median = "sky"
    Hard = "black"

    for card in cards :
       if card.id == card_id:
            for label in card.list_labels:
                if label.color == Easy:
                    penalty = penalty - 50
                    break
                if label.color == Median:
                    penalty = penalty - 30
                    break
                if label.color == Hard:
                    penalty = penalty - 10
                    break
    return penalty

### What is the thing returns???
#performance = {'gyu9': 10, 'yhu22': 20, 'xfu7': 30, 'simtiaz': 20, 'vinay638': 10}
'''
    params:
        trello_username: trello username
        card_id: specific card id under this user
'''
def getPointsOfCard(card_id, cards):
    # find the difficulty level and calculate point
    peformance = 0
    # completeness and difficulty level
    Easy = "yellow"
    Median = "sky"
    Hard = "black"
    Complete = "green"
    Incomplete = "red"
    completemarker = False
    # A Card should have two labels
    for card in cards :
       if card.id == card_id:
            for label in card.list_labels:
                if label.color == Complete:
                    completemarker= True

            for label in card.list_labels:
                if  completemarker== False:
                    print "incomplete"
                    if label.color == Easy:
                        peformance = peformance - 50
                        break
                    if label.color == Median:
                        peformance = peformance - 30
                        break
                    if label.color == Hard:
                        peformance = peformance - 10
                        break
                if  completemarker== True:
                    if label.color == Easy:
                        peformance += 10
                        break
                    if label.color == Median:
                        peformance += 30
                        break
                    if label.color == Hard:
                        peformance += 50
                        break
    return peformance


def getPerformancePoints(intervalLength): # interval Length should be in hours, usually it should be 24
    inactivePenalty = -10
    memberCards = getMemberCardDict() # get member card dict
    #intervalLength = 24 # length of interval, hours
    interval = getInterval(intervalLength)
    performance = {}
    for memberID in memberCards.keys():
        cards = memberCards[memberID]
        completedCards = None
        incompletedCards = None

        completedCards = getAllCompletedCards(memberCards[memberID])
        incompletedCards = getAllIncompletedCards(memberCards[memberID])

        rewardsAndBouns = 0
        penalty = 0

        if completedCards :
            currentCompletedCards = getAllCompletedCardsAtCurrentInterval(completedCards, interval)
            rewardsAndBouns = getRewardsAndBonus(currentCompletedCards)
        if incompletedCards :
            currentIncompleteCards = getAllIncompletedCardsAtCurrentInterval(incompletedCards, interval[1])
            penalty = getPenalty(currentIncompleteCards)
        prevPoint = get_user_points(members_dict[memberID])

        if rewardsAndBouns == 0:
            performance[memberID] = rewardsAndBouns + penalty + prevPoint + inactivePenalty
        else:
            performance[memberID] = rewardsAndBouns + penalty + prevPoint
    memberPerformance = {}
    for memberID in members_dict.keys():
        memberPerformance[members_dict[memberID]] = performance[memberID]
    store_total_points(memberPerformance)
    return memberPerformance

def getPrevTotalPoint():
    prevPoints = {}
    for memberID in members_dict.keys():
        prevPoint = get_user_points(members_dict[memberID])
        prevPoints[members_dict[memberID]] = prevPoint
    return prevPoints

def pushPerformanceToLeaderBoard(performance):
    leaderList = testboard.list_lists()
    for list in leaderList:
        if list.name == "Leader Board":
            cards = list.list_cards()
            for card in cards:
                memberID = card.member_id[0]
                title = "Round x"
                itemName = "Points :" + str(performance[members_dict[memberID]])
                items = [itemName]
                card.add_checklist(title, items)

'''
    params:
        cards: should be the collections of all opened cards, can be get from getAllOpenCards()
        cardID: is the target card whose status should be changed from "to do" to "Done"
        updateCardLabelToComplete
'''
def completeCards(cardID, cards):
    for card in cards:
        if card.id == cardID :
            for label in card.list_labels:
                if label.color == "red":
                    card.remove_label(label)
                    createCardLabel(card, "Done", "green")
                    return

def createCardLabel(card, name, color):
    newLable = client.fetch_json(
        "/cards/" + card.id + "/labels",
        http_method = 'POST',
        post_args = {
            "color": color,
            "name": name
        }
    )

def getUserIncompleteCardsWithInInterval(userID, endTime):
    openCards = getAllOpenCards()
    allCards = []

    for card in openCards:
        if card.member_ids:
            for memberId in card.member_ids:
                if memberId == userID:
                    allCards.append(card)
    incompletedCards = getAllIncompletedCardsAtCurrentInterval(allCards, endTime)
    return incompletedCards

def getAllTargets():
    targetPoints = {}
    for memberID in members_dict.keys():
        targetPoint = get_user_target_points(members_dict[memberID])
        targetPoints[members_dict[memberID]] = targetPoint
    return targetPoints

# member card dict:
# key: member id
# value: a list of card of that member

def getMemberCardDict():
    openCards = getAllOpenCards()
    members = members_dict.keys()
    memberCards = {}
    for member in members:
        memberCards[member] = []

    for card in openCards:
        if card.member_ids:
            for memberId in card.member_ids:
                memberCards[memberId].append(card)
    return memberCards

def updateTargets(intervalLength):
    Easy = "yellow"
    Median = "sky"
    Hard = "black"
    memberCards = getMemberCardDict()

    targetDict = {}
    for memberID in memberCards:
        targetCards = getAllCardsInNextInterval(memberCards[memberID], intervalLength)
        points = 0
        for card in targetCards:
            for label in card.list_labels:
                if label.color == Easy:
                    points += 10
                    break
                if label.color == Median:
                    points += 30
                    break
                if label.color == Hard:
                    points += 50
                    break
        targetDict[members_dict[memberID]] = points
    store_target_points(targetDict)

def getWeekInterval():
    today = datetime.datetime.utcnow()
    weekday = today.weekday()
    monday_delta = datetime.timedelta(weekday)
    sunday_delta = datetime.timedelta(7 - weekday)
    monday = today - monday_delta
    next_monday = today + sunday_delta
    
    monday = dt.combine(monday, dt.min.time())
    monday = monday.replace(tzinfo=pytz.utc)
    next_monday = dt.combine(next_monday, dt.min.time())
    next_monday = next_monday.replace(tzinfo=pytz.utc)
    return (monday, next_monday)

def getAllCardsInNextInterval(cards, intervalLength):
    timeline = getWeekInterval()
    startTime = timeline[0]
    endTime = timeline[1]

    '''startTime = datetime.datetime.utcnow()
    startTime = startTime.replace(tzinfo=pytz.utc)
    endTime = startTime + datetime.timedelta(hours = intervalLength)'''

    targetCards = []
    for card in cards:
        dueDate = card.due_date
        if type(dueDate) == str:
            continue
        if dueDate <= endTime and dueDate >= startTime:
            targetCards.append(card)
    return targetCards

def getInitPerformance(): # interval Length should be in hours, usually it should be 24
    inactivePenalty = -10
    memberCards = getMemberCardDict() # get member card dict
    #intervalLength = 24 # length of interval, hours

    dayInterval = getInterval(24)
    weekInterval = getWeekInterval()
    interval = (weekInterval[0], dayInterval[0])
    performance = {}
    for memberID in memberCards.keys():
        cards = memberCards[memberID]
        completedCards = None
        incompletedCards = None

        completedCards = getAllCompletedCards(memberCards[memberID])
        incompletedCards = getAllIncompletedCards(memberCards[memberID])

        rewardsAndBouns = 0
        penalty = 0

        if completedCards :
            currentCompletedCards = getAllCompletedCardsAtCurrentInterval(completedCards, interval)
            rewardsAndBouns = getRewardsAndBonus(currentCompletedCards)
        if incompletedCards :
            currentIncompleteCards = getAllIncompletedCardsAtCurrentInterval(incompletedCards, interval[1])
            penalty = getPenalty(currentIncompleteCards)
        prevPoint = get_user_points(members_dict[memberID])

        if rewardsAndBouns == 0:
            performance[memberID] = rewardsAndBouns + penalty + prevPoint + inactivePenalty
        else:
            performance[memberID] = rewardsAndBouns + penalty + prevPoint
    memberPerformance = {}
    for memberID in members_dict.keys():
        memberPerformance[members_dict[memberID]] = performance[memberID]
    store_total_points(memberPerformance)
    return memberPerformance

def initPerformancePoint():
    initialPoint = getInitPerformance()
    '''for memberID in members_dict.keys():
        initialPoint[members_dict[memberID]] = 0'''
    store_total_points(initialPoint)    




if __name__ == "__main__":
    var_init()
    ''' start experiments from here '''
    print get_all_names_cards_with_duetime(24)

print "trellocall initialization start"
var_init()
print "trellocall initilization end"
