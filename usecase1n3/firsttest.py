import os
from slackclient import SlackClient
import time
import trellocall
import usecase3
os.environ["BOT_TOKEN"]="xoxb-253135269635-VmnyYnbZdCYdi1YK9r53VK9G"
os.environ["BOT_ID"]="U7F3Z7XJP"
BOT_ID=os.environ.get("BOT_ID")
BOT_TOKEN=os.environ.get("BOT_TOKEN")
AT_BOT = "<@" + BOT_ID + ">"
EXAMPLE_COMMAND = "do"
COMMAND_USECASE_1 = "usecase 1"
COMMAND_USECASE_2 = "usecase 2"
COMMAND_USECASE_3 = "usecase 3"
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
    elif COMMAND_USECASE_1 in command:
        messages=trellocall.print_deadline_messages()
        for m in messages:
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=m, as_user=True)
        #TODO: check it on timely basis
            ''' will be done in milestone 3 '''
        #TODO: send mail to the user
            ''' retrieve mail_id of users from mock.json
            send an email '''
    elif command.startswith(COMMAND_USECASE_2):
        messages=trellocall.print_members_points()
        for key in messages.keys():
            message = str(key) + ": " + str(messages[key])
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=message, as_user=True)
        #todo 
    elif COMMAND_USECASE_3 in command:
        #todo   
        ''' retrieve cards that are due : done
        detect direct message channel for each user: done
        ask for progress: done
        capture response: required
        open a new public channel named "reminderBuddy": required
        post reminders in the channel: required '''
        response="what is your progress, mate?"
        dm_channels=usecase3.perform()
        for d in dm_channels:
            channel=d[2]
            slack_client.api_call("chat.postMessage", channel=channel,
                          text=response, as_user=True)

    else: 
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
                #todo: only works with texts after the mention, need to fix
                return output['text'].split(AT_BOT)[1].strip().lower(), \
                       output['channel']
    return None, None
if __name__ == "__main__":
    READ_WEBSOCKET_DELAY = 1 # 1 second delay between reading from firehose
    if slack_client.rtm_connect():
        print("StarterBot connected and running!")
        while True:
            command, channel = parse_slack_output(slack_client.rtm_read())
            if command and channel: 
                handle_command(command, channel)
            time.sleep(READ_WEBSOCKET_DELAY)
    else:
        print ("Connection failed. Invalid Slack token or bot ID?")
