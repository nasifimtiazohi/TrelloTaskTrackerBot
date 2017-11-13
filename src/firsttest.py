import os
from slackclient import SlackClient
import time
import trellocall
import slackapicall
import usecase3
import usecase1
import thread
# import unicodedata
os.environ["BOT_TOKEN"]='xoxb-266498254006-btD2n1TcKdi5MY6AKlPGTwnm'
os.environ["BOT_ID"]='U7UEN7G06'
# Set Slack BOT environment variables, if failed here, please see the README.md
BOT_ID=os.environ.get("BOT_ID")
BOT_TOKEN=os.environ.get("BOT_TOKEN")

AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
# COMMAND_USECASE_1 = "usecase 1"
COMMAND_USECASE_2 = "show leaderboard"
COMMAND_USECASE_3 = "usecase 3"
P_RESPONSE_USECASE_3 = ['done', '1', 'finished', 'completed', "i'm done", "yes", "of course", "i finished", "yep"]
N_RESPONSE_USECASE_3 = ['pending', '0', 'not yet', 'incomplete', 'wait', 'almost', 'no', 'nah', "i haven't"]

#slack_client = SlackClient(os.environ.get("BOT_TOKEN"))
slack_client= SlackClient(BOT_TOKEN)
def handle_command(command, channel, command_userid):
    """
        Receives commands directed at the bot and determines if they
        are valid commands. If so, then acts on the commands. If not,
        returns back what it needs for clarification.
    """
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    # preprocess the input command to small case and cast from unicode string to string
    command = str(command).lower()

    print("command receive", command)


    #nasif: why is this function not printing leaderboard from the database?
    if command.startswith(COMMAND_USECASE_2):
        messages=trellocall.getPerformancePoints()
        #trellocall.pushPerformanceToLeaderBoard(messages)
        message = "Individual Performance List"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        for key in messages.keys():
            message = str(key) + ": " + str(messages[key])
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        #todo
    # elif COMMAND_USECASE_3 in command:
    #     dm_channels=usecase3.check_progress()
    #     for d in dm_channels:
    #         channel=d[2]
    #         response=d[4]
    #         # cardlist=d[3]
    #         # print "bal",channel
    #         # for c in cardlist:
    #         #     response+=c.name
    #         slack_client.api_call("chat.postMessage", channel=channel,
    #                       text=response, as_user=True)

    # if any(command in s for s in P_RESPONSE_USECASE_3):
    elif command in P_RESPONSE_USECASE_3 and channel not in slackapicall.public_channels():
       print "usecase 3"
       usecase3_post_congratuation_message('C7EK8ECP3', command_userid)
       #update the trello card and also database information
       usecase3.database_init()
       usecase3.reward_points(command_userid, 50)


    # if any(command in s for s in N_RESPONSE_USECASE_3):
    elif command in N_RESPONSE_USECASE_3 and channel not in slackapicall.public_channels():
        #map from command_userid to userid
       d = slackapicall.list_users_byID()
       username = d[command_userid]
       message = "<@" + username +"> " +  "has a task pending, please work harder!"
       slack_client.api_call("chat.postMessage", channel='C7EK8ECP3',
                          text=message, as_user=True)
       #for key in messages.keys():
           #message = str(key) + ": " + str(messages[key])
       #slack_client.api_call("chat.postMessage", channel=channel,
                          #text=message, as_user=True)
    else:
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def usecase3_final_function(threadName, delay):
    while True:
        dm_channels=usecase3.check_progress()
        for d in dm_channels:
            channel=d[2]
            response=d[4]
            slack_client.api_call("chat.postMessage", channel=channel,
                            text=response, as_user=True)
        time.sleep(delay)

def usecase3_post_congratuation_message(channel, userid):
    #Post congraduate message
    #Post only once after the user finished
    #Post to the specific person who respond
    dm_channels=usecase3.post_public_message()
    for d in dm_channels:
        print "Testing: "+ d[0]+  " and " + userid
        if userid == d[0]:
            response=d[4]
            print "The channel is" + channel
            slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)


def parse_slack_output(slack_rtm_output):
    """
        The Slack Real Time Messaging API is an events firehose.
        this parsing function returns None unless a message is
        directed at the Bot, based on its ID.
    """
    output_list = slack_rtm_output
    if output_list and len(output_list) > 0:
        for output in output_list:
            if 'text' in output:
                print output['text']
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                #todo: only works with texts after the mention, need to fix
                print "This current user is responding: "+ output['user']

                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel'],\
                       output['user']
    return None, None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Taskbot connected and running!")
        try:
            #thread.start_new_thread(usecase1.mainFlow,("UC1-mainflow",60*3,))
            #thread.start_new_thread(usecase1.alternateFlow,("UC2-alternateflow",60*5,))
            thread.start_new_thread(usecase3_final_function,("Usecase3",60*3))
        except:
            print "thread could not be started"
        while True:
            command, channel, command_userid = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                    print "handle commands"
                    handle_command(command, channel, command_userid)
            #usecase3_final_function()
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print ("Connection failed. Invalid Slack token or bot ID?")
