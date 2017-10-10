import os
from slackclient import SlackClient
os.environ["firsttest_bot_token"]="xoxb-253135269635-VmnyYnbZdCYdi1YK9r53VK9G"
os.environ["firsttest_bot_id"]="U7F3Z7XJP"
BOT_NAME="firsttest"
slack_client=SlackClient(os.environ.get("firsttest_bot_token"))

if __name__ == "__main__":
    api_call = slack_client.api_call("users.list")
    if api_call.get('ok'):
        # retrieve all users so we can find our bot
        users = api_call.get('members')
        for user in users:
            if 'name' in user and user.get('name') == BOT_NAME:
                print("Bot ID for '" + user['name'] + "' is " + user.get('id'))
    else:
        print("could not find bot user with the name " + BOT_NAME)
else:
    print("balsal")