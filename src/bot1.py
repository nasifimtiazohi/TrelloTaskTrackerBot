import os
from slackclient import SlackClient
from trello import TrelloClient
import time
BOT_ID=os.environ.get("SLACK_BOT_ID")
BOT_TOKEN=os.environ.get("SLACKTOKEN")
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"

userChannel = {}

TRELLO_API_KEY = os.environ.get("TRELLO_API_KEY")
TRELLO_API_SECRET = os.environ.get("TRELLO_API_SECRET")
TRELLO_TOKEN = os.environ.get("TRELLO_TOKEN")

trelloClient = TrelloClient(
    api_key=TRELLO_API_KEY,
    api_secret=TRELLO_API_SECRET,
    token=TRELLO_TOKEN,
    token_secret=None
)
orgs = trelloClient.list_organizations()
for org in orgs:
    print(trelloClient.get_organization(org))
myBoards = trelloClient.list_boards()
boardName = ''
for board in myBoards:
    boardName = boardName + str(board.name) + ' '
    

#slack_client = SlackClient(os.environ.get("BOT_TOKEN"))
slack_client= SlackClient(BOT_TOKEN)
def handle_command(command, channel):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    if command.startswith(EXAMPLE_COMMAND):
        response = "Sure...write some more code then I can do that!" + channel
    slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None
if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    RES = slack_client.rtm_connect()

    users = slack_client.api_call("users.list")
    gyu9ID = ''
    for user in users['members']:
        #userChannel[user['id']] = user['name']
        #print user['name'] + ' ' + user['id']
        if user['name'] == 'gyu9':
            gyu9ID = user['id']
    
    ims = slack_client.api_call("im.list")
    gyu9Channel = ''
    for im in ims['ims']:
        #print im['id']
        #print '\n'
        if im['user'] == gyu9ID:
            gyu9Channel = im['id']
            print slack_client.api_call("chat.postMessage", channel = gyu9Channel,
                                        text = boardName, as_user=True)
        
    if RES:
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                print "current channel is " + channel
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print("Connection failed. Invalid Slack token or bot ID?")
