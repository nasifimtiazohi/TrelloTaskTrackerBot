import os
from slackclient import SlackClient

# BOT_NAME = 'taskbot'
# slack_client = SlackClient(os.environ.get('BOT_TOKEN'))
if not ((os.environ.get('BOT_TOKEN') is None) and (os.environ.get('BOT_ID') is None)):
    print(os.environ.get('BOT_TOKEN'))
    print(os.environ.get('BOT_ID'))
else:
    print('You did not setup the Slack_BOT_Token or BOT_ID. ')
