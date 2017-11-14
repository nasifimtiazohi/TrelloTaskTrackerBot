import os
from slackclient import SlackClient
import time
import trellocall
import slackapicall
import usecase3
import usecase2
import usecase1
import thread
import db_helper

# import unicodedata
os.environ["BOT_TOKEN"]='xoxb-266498254006-btD2n1TcKdi5MY6AKlPGTwnm'
os.environ["BOT_ID"]='U7UEN7G06'
# Set Slack BOT environment variables, if failed here, please see the README.md
BOT_ID=os.environ.get("BOT_ID")
BOT_TOKEN=os.environ.get("BOT_TOKEN")
AT_BOT = "<@" + BOT_ID + ">"
SPLITER = "&gt;"
EXAMPLE_COMMAND = "do"
COMMAND_USECASE_2 = "show leaderboard"
COMMAND_SHOW_TARGET = "show targets board"
COMMAND_USECASE_3 = "usecase 3"
P_RESPONSE_USECASE_3 = ['done', '1', 'finished', 'completed', "i'm done", "yes", "of course", "i finished", "yep"]
N_RESPONSE_USECASE_3 = ['pending', '0', 'not yet', 'incomplete', 'wait', 'almost', 'no', 'nah', "i haven't"]
RESET_TOTAL_SCORES = "reset leaderboard"

# slackname_to_trelloname = {
#         'simtiaz':'sheikhnasifimtiaz',
#         'gyu9':"guanxuyu",
#         'xfu7':'xiaotingfu1',
#         'vgupta8':'vinay638',
#         'yhu22': 'otto292'}

#slack_client = SlackClient(os.environ.get("BOT_TOKEN"))
slack_client= SlackClient(BOT_TOKEN)


###############################################################################
#                    Handle Command for Usecase 2                             #
###############################################################################
# params:
#         command: string, the parsed command from slack user output
#         channel: the target channel to post message
#                                                                             #
###############################################################################
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
    print("Command received: ", command)
    #nasif: why is this function not printing leaderboard from the database?
    if command.startswith(COMMAND_USECASE_2):
        messages=trellocall.getPrevTotalPoint()
        #trellocall.pushPerformanceToLeaderBoard(messages)
        message = "Individual Performance List"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        for key in messages.keys():
            message = str(key) + ": " + str(messages[key])
            if str(key) == 'vinay638':
                message = str(key) + ":                 " + str(messages[key])
            if str(key) == 'otto292':
                message = str(key) + ":                   " + str(messages[key])
            if str(key) == 'xiaotingfu1':
                message = str(key) + ":             " + str(messages[key])
            if str(key) == 'sheikhnasifimtiaz':
                message = str(key) + ":   " + str(messages[key])
            if str(key) == 'guanxuyu':
                message = str(key) + ":                " + str(messages[key])
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
    elif command.startswith(COMMAND_SHOW_TARGET):
        messages=trellocall.getAllTargets()
        #trellocall.pushPerformanceToLeaderBoard(messages)
        message = "Individual Target List"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        for key in messages.keys():
            message = str(key) + ": " + str(messages[key])
            if str(key) == 'vinay638':
                message = str(key) + ":                 " + str(messages[key])
            if str(key) == 'otto292':
                message = str(key) + ":                   " + str(messages[key])
            if str(key) == 'xiaotingfu1':
                message = str(key) + ":             " + str(messages[key])
            if str(key) == 'sheikhnasifimtiaz':
                message = str(key) + ":   " + str(messages[key])
            if str(key) == 'guanxuyu':
                message = str(key) + ":                " + str(messages[key])
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
    elif command in N_RESPONSE_USECASE_3 and channel not in slackapicall.public_channels():
        #map from command_userid to userid
       d = slackapicall.list_users_byID()
       slack_username = d[command_userid]
       trello_username = trellocall.slackname_to_trelloname[slack_username]
       message = "<@" + command_userid +"> " +  "has a task pending, please work harder!"
       slack_client.api_call("chat.postMessage", channel='C7EK8ECP3',
                          text=message, as_user=True)
    elif command in RESET_TOTAL_SCORES and channel not in slackapicall.public_channels():
       print "Reset the leaderboard..."
       db_helper.total_points_init()
       db_helper.print_leaderboard() 
    else:
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

##########################################################################################
#                               Handle Command for Usecase 3                             #
##########################################################################################
# params:                                                                                #
#         command: string, the parsed command from slack user output                     #
#         channel: the target channel to post message                                    #
#         command_userid: the parsed id of slack user who initialized this command       #
#         command_card_id: the parsed name of the task card which belong to this user    #
#                                                                                        #
##########################################################################################
def handle_command_for_usecase3(command, channel, command_userid, command_cardname):
    response = "Not sure what you mean. Use the *" + EXAMPLE_COMMAND + \
               "* command with numbers, delimited by spaces."
    command = str(command).lower()
    print("Command Received:", command)
    if command in P_RESPONSE_USECASE_3 and channel not in slackapicall.public_channels():
       # Get a dictionary which map slack user id to the user name
       slackIdToNameDict = slackapicall.list_users_byID()
       # Get Slack user name by slack user id
       slack_username = slackIdToNameDict[command_userid]
       # Get trello name from slack name
       trello_username = trellocall.slackname_to_trelloname[slack_username]
       # map from command_userid to trello_username
       print "Debug: trello_username: " + trello_username
       print "Debug: command_cardname: " + command_cardname
       # IMPORTANT: Search from database and Map
       # Init Database before searching it
       db_helper.database_init()
       card_id = db_helper.getCardIdbyCardName(trello_username, command_cardname)
       #DO 0: Update database Set progress to "Completed"
       print "DO 0: Update database Set progress to Completed"
       if card_id != None:
            print "Debug: card_id: " + card_id
            db_helper.update_progres(trello_username, card_id)
            #DO 4: update trello label
            print "DO 4: update trello label"
            # get the list of due cards of this user
            duecardlist = []
            users_with_duecards=trellocall.trelloname_with_duetime(20)
            for user in users_with_duecards.keys():
                if user == trello_username:
                    print "inside if 1: " + user
                    #Get all cards belong to this user
                    duecardlist=users_with_duecards[user]
            # BUG: duecard info is not updated after the label is updated
            trellocall.completeCards(card_id,duecardlist)
            # TODO: get all cards of the user twice
            users_with_duecards2=trellocall.trelloname_with_duetime(20)
            time.sleep(2)
            cardlist = trellocall.get_all_cards_of_user(trello_username)

            if db_helper.get_progress_of_card(trello_username, card_id) == "Completed" and db_helper.check_if_done(trello_username, card_id) == "false":
                        #DO 1: Update performance point
                        db_helper.update_congratualtion_status(trello_username, card_id) # set is_congratulated to "true"
                        reward_point =  trellocall.getPointsOfCard(card_id, cardlist) # update point in database
                        print "reward_point: " + str(reward_point)
                        db_helper.reward_points(trello_username,reward_point)
                        #DO 2: Post congratulation message to this user
                        usecase3_post_congratuation_message('C7EK8ECP3', command_userid)
                        #DO 3: Post performance score to this user
                        #DO 4: Update total point
                        # TypeError: coercing to Unicode: need string or buffer, int found
                        message = "<@" + command_userid + ">" + ", you earned: "+ str(reward_point) + " points for finishing this task. Now, your performance score have been updated to: " + str(db_helper.get_user_points(trello_username))
                        slack_client.api_call("chat.postMessage", channel='C7EK8ECP3',text=message, as_user=True)

       else:
            # If cannot find command in the database, prompt user to input again
            message = "Well, your status is: " + command + ", however, the task you input seems incorrect, please try again..."
            slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)

def usecase3_final_function(threadName, delay):
    while True:
        dm_channels=usecase3.check_progress()
        for directMessage in dm_channels:
            channel=directMessage[2]
            response=directMessage[4]
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
                #if SPLITER in output['text']:
                     return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel'],\
                       output['user']
    return None, None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Taskbot connected and running!")
        try:
            thread.start_new_thread(usecase1.mainFlow,("UC1-mainflow",60*3,))
            thread.start_new_thread(usecase1.alternateFlow,("UC2-alternateflow",60*5,))
            thread.start_new_thread(usecase2.mainFlow, ("Usecase2", 24*60*60))
            thread.start_new_thread(usecase3_final_function,("Usecase3",60*3))
        except:
            print "thread could not be started"
        while True:
                command, channel, command_userid= parse_slack_output(slack_client.rtm_read())
                if command and channel and command_userid:
                    if SPLITER in command:
                        #use case 3
                        command_cardname = command.split(SPLITER)[1].strip().lower()
                        command = command.split(SPLITER)[0].strip().lower()
                        print "command: " + command
                        print "command cardname: " + command_cardname
                        print "command userid: " + command_userid
                        handle_command_for_usecase3(command, channel, command_userid, command_cardname)
                    else:
                        #use case 2, no need for further parse of string
                        handle_command(command, channel, command_userid)
              #usecase3_final_function()
        time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print ("Connection failed. Invalid Slack token or bot ID?")
