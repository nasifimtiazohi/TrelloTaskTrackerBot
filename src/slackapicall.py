from slackclient import SlackClient
import os
import json
import requests

'''
firsttest   U7F3Z7XJP
gyu9   U7FMUT4HJ
simtiaz   U7EK8EBAM
test_bot   U7MURQ2F6
trello   U7FBA0CRK
vgupta8   U7HDGGXKR
xfu7   U7GLR2L6T
yhu22   U7FL172BU
slackbot   USLACKBOT
'''
os.environ["BOT_TOKEN"]='xoxb-266498254006-btD2n1TcKdi5MY6AKlPGTwnm'
os.environ["BOT_ID"]='U7UEN7G06'
BOT_ID=os.environ.get("BOT_ID")
BOT_TOKEN=os.environ.get("BOT_TOKEN")

#print BOT_TOKEN
slack_client= SlackClient(BOT_TOKEN)

def name_to_id(username):
    d=list_users()
    return d[username]

def fullname_to_id(fullname):
    d={}
    call= slack_client.api_call("users.list")
    users=call['members']
    for c in users:
        profile=c['profile']
        d[profile['real_name'].lower()]=c['id']
    return d[fullname]
    

def open_im(user_id):
    f=True
    url = 'https://slack.com/api/im.open'
    headers = {'content-type':'x-www-form-urlencoded'}
    data = [('token', BOT_TOKEN), ('user', user_id),('include_local',f),('return_im',f) ]
    r= requests.post(url,data,headers )
    d=json.loads(r.text)
    channel=d['channel']
    channel_id=channel['id']
    print channel_id
    return channel_id

def list_channels():
    call= slack_client.api_call("channels.list")
    channels=call["channels"]
    for c in channels:
        print c['name']," ",c['id']
    if call.get("ok"):
        return call["channels"]
    else:
        return None



def list_users():
    d={}
    call= slack_client.api_call("users.list")
    users=call['members']
    for c in users:
        # profile=c['profile']
        # if 'email' in profile.keys():
        #     print profile['email']
        #     print profile['real_name']
        d[c['name']]=c['id']
    return d

def nameNmail():
    d={}
    call= slack_client.api_call("users.list")
    users=call['members']
    for c in users:
        profile=c['profile']
        if 'email' in profile.keys():
            # print profile['email']
            # print profile['real_name']
            d[profile['real_name'].lower()]=profile['email']
    return d



if __name__== "__main__":
    print list_users()
