from trello import TrelloClient
import fetch_from_db
import struct
import datetime
import os
import pytz
import slackapicall
import json
import emailing

members_dict=None
project_team=None
testboard=None
mockdata=None
trelloKey='dbf6947f87a8dcb83f090731a27e8bd4'
trelloSecret='f57a6c66081742aa5f6149d329c3581d53231c308e4cc9f78b31230ce13b3bb8'
trelloToken='414df911de9e839c8ab9838c8fa1723107fba5848e5049269d88e5e94a348f31'

#TODO: Usecase3 only asks a person about progress. No matter how many cards are due. Later we'll refine it

client = TrelloClient(
    api_key = trelloKey,
    api_secret=trelloSecret,
    token=trelloToken,
    token_secret=None
)


def get_all_cards_with_duedate():
    current_time=datetime.datetime.now()
    current_time=current_time.replace(tzinfo=pytz.utc)
    opencards=testboard.open_cards()
    duecards=[]
    for c in opencards:
        temp=c.due_date
        if c.due_date:
            temp=temp.replace(tzinfo=pytz.utc)
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
            temp=temp.replace(tzinfo=pytz.utc)
            temp2=temp-datetime.timedelta(hours=timeinhours)
            if current_time<temp and current_time>temp2 and '59bdb4181314a33999a2736d' not in c.label_ids:
                duecards.append(c)
    return duecards

def get_all_names_cards_with_duetime(timeinhours):
    current_time=datetime.datetime.now()
    current_time=current_time.replace(tzinfo=pytz.utc)
    print "hello",testboard.name
    opencards=testboard.open_cards()
    duecards=[]
    for c in opencards:
        temp=c.due_date
        if c.due_date:
            temp=temp.replace(tzinfo=pytz.utc)
            temp2=temp-datetime.timedelta(hours=timeinhours)
            if current_time<temp and current_time>temp2 and '59bdb4181314a33999a2736d' not in c.label_ids:
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


def print_deadline_messages():
    message_list=[]
    lists=testboard.all_lists()
    for l in lists:
        if l.name=="task within 1 day deaadline":
            target_list=l
            break
    cards=target_list.list_cards()
    members = project_team.get_members()
    #todo: make it a dictionary for easy searching
    for c in cards:
        target_card=c
        message=""
        #todo:only search for the first member. make it about all
        mid=target_card.member_id
        for m in members:
            if m.id==mid[0]:
                message+=m.username
                name=m.username
                break
        message+=" is asked to complete " + c.name
        print message
        sendmail(name,message)
        message_list.append(message)
    return message_list

def sendmail(name,message):
    #print name
    temp=mockdata['trello_name_to_mailid']
    mail=temp[name]
    #print mail
    emailing.sendmail(mail,message)

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
    global mockdata
    teams=client.list_organizations()
    for t in teams:
        if t.name=='510projectteam':
            project_team=t
            break
    boards = project_team.get_boards(project_team)
    for b in boards:
        if b.name=='Test Board':
            testboard=b
    members_dict=members_dictionary(project_team)
    with open('mock.json') as json_data:
        mockdata = json.load(json_data)

''' def match_trello_slack_id():
    userlist= slackapicall.list_users()
    namelist_with_duecards=get_all_cards_with_duedate()
    print mockdata['idmatching']
    for n in namelist_with_duecards:
        print n
    print "here's a gap"
    for d in userlist:
        print d['slackname'] '''
    

def slackname_with_duecards():
    trelloname_with_duecards=get_all_cards_with_duedate()
    ''' read mock data for matching for now
    in future match by mail id? '''
    slackname_with_duecrds={}
    mapping = mockdata["trello_to_slack_name"]

    for n in trelloname_with_duecards.keys():
        slackname=mapping[n]
        slackname_with_duecrds[slackname]=trelloname_with_duecards[n]
    return slackname_with_duecrds


def slackname_with_duetime(duetime_in_hours):
    trelloname_with_duecards=get_all_names_cards_with_duetime(duetime_in_hours)
    ''' read mock data for matching for now
    in future match by mail id? '''
    slackname_with_duecrds={}
    mapping = mockdata["trello_to_slack_name"]
    
    for n in trelloname_with_duecards.keys():
        slackname=mapping[n]
        slackname_with_duecrds[slackname]=trelloname_with_duecards[n]
    return slackname_with_duecrds

def print_members_points():
    teams = client.list_organizations()
    for team in teams:
        teamID=team.id
        #todo: if there's more than one organization?
    curTeam=client.get_organization(teamID)
    boards = curTeam.get_boards(curTeam)
    members = curTeam.get_members()
    idMembersDict = {}
    membersPoint = {}
    for member in members:
        membersPoint[member.username] = 0
    for member in members:
        idMembersDict[member.id] = member.username
    for board in boards:
        testBoard=board
        #todo: if there's more than one board?
    lists=testBoard.list_lists()
    for list in lists:
        if list.name == "Leader Board":
            cards=list.list_cards()
            #todo: make it a dictionary for easy searching
            for card in cards:
                membersID = card.member_id
                checkLists = card.fetch_checklists()
                for checkList in checkLists:
                    items = checkList.items
                    for item in items:
                        points = item["name"].split(' ')[0]
                        for memberID in membersID:
                            membersPoint[idMembersDict[memberID]] += int(points)
    return membersPoint


def getInterval(timeInHours):
    endTime = datetime.datetime.utcnow()
    endTime = endTime.replace(tzinfo=pytz.utc)
    startTime = endTime - datetime.timedelta(hours = timeInHours)
    return (startTime, endTime)

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
                    '''if card.due_date:
                        dueDate = card.due_date
                        dueDate = dueDate.replace(tzinfo=pytz.utc)
                        if dueDate < currentTime:'''
                    inCompletedCards.append(card)
    return inCompletedCards

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
        dueDate = dueDate.replace(tzinfo=pytz.utc)
        if dueDate < endTimePoint:
            currentIncompleteCards.append(card)
    return currentIncompleteCards

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

def getPerformancePoints():
    openCards = getAllOpenCards()

    members = members_dict.keys()
    memberCards = {}

    for member in members:
        memberCards[member] = []

    for card in openCards:
        if card.member_ids:
            for memberId in card.member_ids:
                memberCards[memberId].append(card)

    intervalLength = 5 # length of interval, hours
    interval = getInterval(5)
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
        prevPoint = fetch_from_db.get_user_points(members_dick[memberID])
        performance[memberID] = rewardsAndBouns + penalty + prevPoint
    memberPerformance = {}
    for memberID in members_dict.keys():
        memberPerformance[members_dict[memberID]] = performance[memberID]
    fetch_from_db.store_total_points(memberPerformance)
    return memberPerformance

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


if __name__ == "__main__":
    var_init()
    ''' read mock data '''
    ''' start experiments from here '''
    d=slackname_with_duecards()
    print d

    
    
            

print "trellocall initialization start"
var_init()
print "trellocall initilization end"



    

    
    
