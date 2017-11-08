import os
from slackclient import SlackClient

'''Make sure to set up the Slack BOT token and ID'''
if not ((os.environ.get('BOT_TOKEN') is None) or (os.environ.get('BOT_ID') is None)):
    print(os.environ.get('BOT_TOKEN'))
    print(os.environ.get('BOT_ID'))
else:
    print('You did not setup the Slack_BOT_Token or BOT_ID. ')
