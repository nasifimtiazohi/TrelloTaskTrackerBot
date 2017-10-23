from trello import TrelloClient
import struct


trelloToken = 'fafbd8bea1ca07b19f8656b62174b81d7dbed73bdddaf318b61192bce9931ab3'
trelloKey = 'cda12dfc52f6530a3eb17745f1b4e61b'
trelloSecret = '96d037afb64bfb3306bd031bd403b1eeca1836186e0c09109b1a03ad5aec1c11'

client = TrelloClient(
    api_key = trelloKey,
    api_secret=trelloSecret,
    token=trelloToken,
    token_secret=None
)

def print_deadline_messages():
    message_list=[]
    teams = client.list_organizations()
    for t in teams:
        project_team_id=t.id
        #todo: if there's more than one organization?
    project_team=client.get_organization(project_team_id)
    boards = project_team.get_boards(project_team)
    for b in boards:
        testboard=b
        #todo: if there's more than one board?
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
        mid=target_card.member_id
        for m in members:
            if m.id==mid[0]:
                message+=m.username
        message+=" is asked to complete " + c.name
        print message
        message_list.append(message)
    return message_list


if __name__ == "__main__":
    ''' all_boards = client.list_boards()
    for board in all_boards:
        print board.name '''
    messages=print_deadline_messages()
    for m in messages:
        print "sdsd"+m

    
    
