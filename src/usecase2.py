from trello import TrelloClient
import os
import struct

TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")
TRELLO_API_SECRET = os.environ.get("TRELLO_API_SECRET")
TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

client = TrelloClient(
    api_key = TRELLO_API_KEY,
    api_secret=TRELLO_API_SECRET,
    token=TRELLO_TOKEN,
    token_secret=None
)

def countPersonalPoints(client):
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
    messages = ""
    for key in membersPoint.keys():
        messages = messages + str(key) + ": "
        messages = messages + str(membersPoint[key])
    return messages

if __name__ == "__main__":
    dict = countPersonalPoints(client)
    print(dict)