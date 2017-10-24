from trello import TrelloClient
import struct
import datetime
import os
import pytz
import slackapicall
import json
import emailing
# import sys
# os.environ['DJANGO_SETTINGS_MODULE'] = '/home/nasif/tools/510project/bot510/bot510/bot510.settings'
# from django.utils import timezone

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
    teams = client.list_organizations()
    for t in teams:
        project_team_id=t.id
        #todo: if there's more than one organization?
    project_team=client.get_organization(project_team_id)
    boards = project_team.get_boards(project_team)
    for b in boards:
        testboard=b
        #todo: if there's more than one board?
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
    namelist_with_duecards=[]
    for c in duecards:
        mid=c.member_id[0]
        name=members_dict[mid]
        if name not in namelist_with_duecards:
            namelist_with_duecards.append(name)
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
    print name
    temp=mockdata['trello_name_to_mailid']
    mail=temp[name]
    print mail
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
    teams = client.list_organizations()
    for t in teams:
        project_team_id=t.id
        #todo: if there's more than one organization?
    project_team = client.get_organization(project_team_id)
    boards = project_team.get_boards(project_team)
    for b in boards:
        testboard=b
        #todo: if there's more than one board?
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
    slackname_with_duecrds=[]
    mapping = mockdata["trello_to_slack_name"]
    for n in trelloname_with_duecards:
        slackname_with_duecrds.append(mapping[n])
    return slackname_with_duecrds
  
if __name__ == "__main__":
    var_init()
    ''' read mock data '''
    ''' start experiments from here '''
    print_deadline_messages()

print "trellocall initialization start"
var_init()
print "trellocall initilization end"


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
    

    
    
