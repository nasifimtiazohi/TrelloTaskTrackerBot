import os
from slackclient import SlackClient
import time
import trellocall
import usecase3
import usecase1
os.environ["BOT_TOKEN"]='xoxb-266498254006-btD2n1TcKdi5MY6AKlPGTwnm'
os.environ["BOT_ID"]='U7UEN7G06'
BOT_ID=os.environ.get("BOT_ID")
BOT_TOKEN=os.environ.get("BOT_TOKEN")
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
COMMAND_USECASE_1 = "usecase 1"
COMMAND_USECASE_2 = "usecase 2"
COMMAND_USECASE_3 = "usecase 3"
P_RESPONSE_USECASE_3 = "1"
N_RESPONSE_USECASE_3 = "0"

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
        response = "Sure...write some more code then I can do that!"
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    elif command.startswith(COMMAND_USECASE_2):
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
    elif COMMAND_USECASE_3 in command:
        dm_channels=usecase3.check_progress()
        for d in dm_channels:
            channel=d[2]
            response=d[4]
            # cardlist=d[3]
            # print "bal",channel
            # for c in cardlist:
            #     response+=c.name
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
                          
    elif command.startswith(P_RESPONSE_USECASE_3):
       usecase3_post_congratuation_message()

    elif command.startswith(N_RESPONSE_USECASE_3):
       #trellocall.pushPerformanceToLeaderBoard(messages)
       message = "Alright, your response is pending, please work harder!"
       slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
       for key in messages.keys():
           message = str(key) + ": " + str(messages[key])
           slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
    else:
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

def usecase3_final_function():
    #response="what is your progress, mate?"
    #print ("is it getting called?")
    dm_channels=usecase3.check_progress()
    for d in dm_channels:
        channel=d[2]
        response=d[4]
            # cardlist=d[3]
            # print "bal",channel
            # for c in cardlist:
            #     response+=c.name
        slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)
    #time.sleep(60*3)
    
def usecase3_post_congratuation_message():
    #Post congraduate message
    #Post only once after the user finished
    dm_channels=usecase3.post_public_message()
    for d in dm_channels:
        channel=d[2]
        response=d[4]
        print "The channel is" + channel
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
            if 'text' in output:
                print output['text']
            if output and 'text' in output and AT_BOT in output['text']:
                # return text after the @ mention, whitespace removed
                #todo: only works with texts after the mention, need to fix
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None

if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("Taskbot connected and running!")
        while True:
            #usecase1.perform()
            usecase3_final_function()
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel:
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print ("Connection failed. Invalid Slack token or bot ID?")
