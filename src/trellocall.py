from trello import TrelloClient
from trello import label as trelloLabel
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

# Set up Trello environment variables, if failed here, please see the README.md
trelloKey = os.environ.get("TRELLO_API_KEY")
trelloSecret = os.environ.get("TRELLO_API_SECRET")
trelloToken = os.environ.get("TRELLO_TOKEN")

#TODO: Usecase3 only asks a person about progress. No matter how many cards are due. Later we'll refine it

client = TrelloClient(
    api_key = trelloKey,
    api_secret=trelloSecret,
    token=trelloToken,
    token_secret=None
)
# return a list of things:
# card_id, user_id, due_date, card_name, points, progress
def get_all_cards_of_user():
    opencards = testboard.open_cards()
    all_card_info=[]
    #print "The performance point: "+getPerformancePoints()
    for c in opencards:
        card_info = []
        for userid in c.member_ids:
            user_name = members_dict[userid]
            # 'sheikhnasifimtiaz' is a slack name
            #if user_name == 'sheikhnasifimtiaz':
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
                card_info.append(user_name)
                card_info.append(card_id)
                card_info.append(userid)
                #card_info.extend((due_date, userid, due_date, card_name, user_name, progress))
                all_card_info.append(card_info)
            #points = getPerformancePoints()[userid]
            #progress = getCardProgress(card_id)
            #how to know if the card is due or not
            #card_info.append(card_id, userid, due_date, card_name, points, progress)
    return all_card_info

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

def slack_name_to_trello_name(slack_name):
     mapping = mockdata["slack_name_to_trello_name"]
     return mapping[slack_name]

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
    '''
    read mock data for matching for now,
    in future match by mail id?
    '''
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

### What is the thing returns???
#performance = {'gyu9': 10, 'yhu22': 20, 'xfu7': 30, 'simtiaz': 20, 'vinay638': 10}

def updatePerformancePoints():
    #....
    hello

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
        prevPoint = fetch_from_db.get_user_points(members_dict[memberID])
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

'''
    params:
        cards: should be the collections of all opened cards, can be get from getAllOpenCards()
        cardID: is the target card whose status should be changed from "to do" to "Done"
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


if __name__ == "__main__":
    var_init()
    ''' read mock data '''
    ''' start experiments from here '''
    d=slackname_with_duecards()
    print d





print "trellocall initialization start"
var_init()
print "trellocall initilization end"
