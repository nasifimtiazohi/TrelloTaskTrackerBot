from trello import TrelloClient
import struct


trelloKey='dbf6947f87a8dcb83f090731a27e8bd4'
trelloSecret='f57a6c66081742aa5f6149d329c3581d53231c308e4cc9f78b31230ce13b3bb8'
trelloToken='414df911de9e839c8ab9838c8fa1723107fba5848e5049269d88e5e94a348f31'

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
    lists=testboard.list_lists()
    for l in lists:
        if l.name=="Bot Milestone: Week 1":
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
            if m.id in mid:
                message+=m.username + " "

        message+=" is asked to complete " + c.name
        print message
        message_list.append(message)
    return message_list

if __name__ == "__main__":
    messages=print_deadline_messages()