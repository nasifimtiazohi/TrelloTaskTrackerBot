import os
from slackclient import SlackClient
import time
import trellocall
import slackapicall
import usecase3
import usecase2
import usecase1
import usecase2
import thread
import db_helper

# Set Slack BOT environment variables, if failed here, please see the README.md
# f = open("/home/ubuntu/dev/src/token.txt","r")
# token = []
# for l in f:
#   l=l.rstrip('\n')
#   token.append(l)

# BOT_ID=token[3]
# BOT_TOKEN=token[2]
BOT_ID=os.environ.get("BOT_ID")
BOT_TOKEN=os.environ.get("BOT_TOKEN")
AT_BOT = "<@" + BOT_ID + ">"
SPLITER = "&gt;"
EXAMPLE_COMMAND = "do"
COMMAND_USECASE_2 = "show leaderboard"
COMMAND_SHOW_TARGET = "show targets board"
COMMAND_USECASE_3 = "usecase 3"
P_RESPONSE_USECASE_3 = ['done', '1', 'finish','finished', 'completed', "i'm done", "yes", "of course", "i finished", "yep", 'yeah']
N_RESPONSE_USECASE_3 = ['pending', '0', 'not yet', 'incomplete', 'wait', 'almost', 'no', 'nah', "i haven't", 'nope']
RESET_TOTAL_SCORES = "reset leaderboard"

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
    response = "Not sure what you mean. Use the proper commands... "
    # preprocess the input command to small case and cast from unicode string to string
    command = str(command).lower()
    print("Command received: ", command, "nasif")
    if command.startswith(COMMAND_USECASE_2):
        messages=trellocall.getPrevTotalPoint()
        #trellocall.pushPerformanceToLeaderBoard(messages)
        message = "Individual Performance List"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        #sort it maybe?
        for key in messages.keys():
            if "bot" in str(key):
                continue
            message = str(key) + ": " + str(messages[key])
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
    elif command.startswith(COMMAND_SHOW_TARGET):
        messages=trellocall.getAllTargets()
        #trellocall.pushPerformanceToLeaderBoard(messages)
        message = "Individual Target List"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        for key in messages.keys():
            if "bot" in str(key):
                continue
            message = str(key) + ": " + str(messages[key])
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
    elif command in RESET_TOTAL_SCORES:
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
    response = "Not sure what you mean. Use the proper commands... "
    command = str(command).lower()
    # print("Command Received:", command, "fu"
    slackIdToNameDict = slackapicall.list_users_byID()
                # Get Slack user name by slack user id
    slack_username = slackIdToNameDict[command_userid]
                # Get trello name from slack name
    trello_name = trellocall.slackname_to_trelloname(slack_username)
    if command in N_RESPONSE_USECASE_3 and channel not in slackapicall.public_channels():
       # IMPORTANT: Search from database and Map
       # Init Database before searching it
       db_helper.database_init()
       print ("debug latest:",trello_name,command_cardname)
       card_id = db_helper.getCardIdbyCardName(trello_name, command_cardname)
       if card_id != None:
              users_with_cards=trellocall.slackname_with_duetime(24)
              for slack_name in users_with_cards.keys():
                # TODO: Fix bug here
                # Slack user id 
                print ("debug: which name?",slack_name)
                try:
                    userid=slackapicall.fullname_to_id(slack_name)
                    cardlist=users_with_cards[slack_name]
                    # find the user of the card
                    for card in cardlist:
                         if card_id == card.id:
                            message= "<@"+userid+"> ," +" has a task pending: " + card.name + " , please work harder!"
                            slack_client.api_call("chat.postMessage", channel=slackapicall.get_general_channel_id(),
                                    text=message, as_user=True)
                except:
                    cardlist=users_with_cards[slack_name]
                    # find the user of the card
                    for card in cardlist:
                        if card_id == card.id:
                            message= slack_name+" has a task pending: " + card.name + " , please work harder!"
                            slack_client.api_call("chat.postMessage", channel=slackapicall.get_general_channel_id(),
                                    text=message, as_user=True)
       else:
            # If cannot find command in the database, prompt user to input again
            message = "Well, your status is: " + command + ", however, the task you input seems incorrect, please try again..."
            slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)
                          
        #message = "<@" + command_userid +"> " +  "has a task pending, please work harder!"
    elif command in P_RESPONSE_USECASE_3 and channel not in slackapicall.public_channels():
       # IMPORTANT: Search from database and Map
       # Init Database before searching it
       db_helper.database_init() 
       card_id = db_helper.getCardIdbyCardName(trello_name, command_cardname)
       #DO 0: Update database Set progress to "Completed"
       #TODO: Update database to set each person of the same card's progress as complete
       print "DO 0: Update database Set progress to Completed"
       if card_id != None:
            print "Debug: card_id: " + card_id
            #users_with_cards=trellocall.slackname_with_duetime(24)
            # Get Slack user name by slack user id
            slack_name = slackIdToNameDict[command_userid]
            # Get trello name from slack name
            trello_name = trellocall.slackname_to_trelloname(slack_name)
            duecardlist = []

            users_with_duecards=trellocall.trelloname_with_duetime(24)
            for user in users_with_duecards.keys():
                if user == trello_name:
                    print "inside if 1: " + user
                    #Get all cards belong to this user
                    duecardlist=users_with_duecards[user]
            #DO 4: update trello label
            print "DO 4: update trello label"
            trellocall.completeCards(card_id,duecardlist) # When one member mark the card as complete, our member shall also not get notification, since this card is complete
            
            for trello_username in users_with_duecards.keys():
                # get a list of user of this card
                        print "trello_name: " + trello_username
                        #userid=slackapicall.fullname_to_id(slack_name)
                        cardlist=users_with_duecards[trello_username]
                        # Get Slack user name by slack user id
                        #slack_username = slackIdToNameDict[userid]
                        # Get trello name from slack name
                        #trello_username = trellocall.slackname_to_trelloname(slack_username)
                        # map from command_userid to trello_username
                        print "Debug: trello_username: " + trello_username
                        print "Debug: command_cardname: " + command_cardname
                        db_helper.update_progres(trello_username, card_id) #set progress to completed
                        time.sleep(2)
                        cardlist = trellocall.get_all_cards_of_user(trello_username)
                        if db_helper.get_progress_of_card(trello_username, card_id) == "Completed" and db_helper.check_if_done(trello_username, card_id) == "false":
                                    #DO 1: Update performance point
                                    db_helper.update_congratualtion_status(trello_username, card_id) # set is_congratulated to "true"
                                    reward_point =  trellocall.getPointsOfCard(card_id, cardlist) # update point in database
                                    print "reward_point: " + str(reward_point)
                                    db_helper.reward_points(trello_username,reward_point)
                                    #DO 2: Post congratulation message to this user
                                    message1="Congratulations to <@"+ trello_username+"> ," +" for finishing the task before the deadline!"
                                    slack_client.api_call("chat.postMessage", channel=slackapicall.get_general_channel_id(),text=message1, as_user=True)
                                    #DO 3: Post performance score to this user
                                    message = "<@" + trello_username + ">" + ", you earned: "+ str(reward_point) + " points for finishing this task. Now, your performance score have been updated to: " + str(db_helper.get_user_points(trello_username))
                                    slack_client.api_call("chat.postMessage", channel=slackapicall.get_general_channel_id(),text=message, as_user=True)
                        elif db_helper.get_progress_of_card(trello_username, card_id) == "Completed" and db_helper.check_if_done(trello_username, card_id) == "true":
                            # The user has completed the task and is congratulated, don't congras again
                            message = "Either you or your team mate have completed this task: " + ", we have your record, no need to report again! "
                            slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)
                    
       else:
            # If cannot find command in the database, prompt user to input again
            message = "Well, your status is: " + command + ", however, the task you input seems incorrect, please try again..."
            slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)
    elif channel in slackapicall.public_channels():
        message = "Public channel is not for updating your task progress. Please go in private channel with me!"
        slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)
    else:
        message = "Not sure what you mean! Use the proper commands..."
        slack_client.api_call("chat.postMessage", channel=channel,text=message, as_user=True)

def usecase3_final_function(threadName, delay):
    while True:
        print "in usecase 3"
        dm_channels=usecase3.check_progress()
        for directMessage in dm_channels:
            channel=directMessage[2]
            response=directMessage[4]
            slack_client.api_call("chat.postMessage", channel=channel,
                            text=response, as_user=True)
        time.sleep(delay)

# def usecase3_post_congratuation_message(channel, userid):
#     #Post congraduate message
#     #Post only once after the user finished
#     #Post to the specific person who respond
#     dm_channels=usecase3.post_public_message()
#     for d in dm_channels:
#         print "Testing: "+ d[0]+  " and " + userid
#         if userid == d[0]:
#             response=d[4]
#             print "The channel is" + channel
#             slack_client.api_call("chat.postMessage", channel=channel, text=response, as_user=True)

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
            thread.start_new_thread(usecase1.mainFlow,("UC1-mainflow",60*60,))
            thread.start_new_thread(usecase1.alternateFlow,("UC2-alternateflow",60*60,))
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
