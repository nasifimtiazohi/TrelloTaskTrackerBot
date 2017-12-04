from slackclient import SlackClient
import os
import json
import requests

# f = open("/home/ubuntu/dev/src/token.txt","r")
# token = []
# for l in f:
#   l=l.rstrip('\n')
#   token.append(l)

# BOT_ID=token[3]
# BOT_TOKEN=token[2]

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
    print (call)
    if 'members' in call.keys():
        print("debug: it eneter here")
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
def get_general_channel_id():
    call= slack_client.api_call("channels.list")
    channels=call["channels"]
    for c in channels:
        if c['name']=="general":
            return c['id']
    return None
def public_channels():
    call= slack_client.api_call("channels.list")
    channels=call["channels"]
    res=[]
    for c in channels:
        res.append(c['id'])
    return res


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

def list_users_byID():
    d={}
    call= slack_client.api_call("users.list")
    users=call['members']
    for c in users:
        # profile=c['profile']
        # if 'email' in profile.keys():
        #     print profile['email']
        #     print profile['real_name']
        d[c['id']]=c['name']
    return d
def fullnameNname():
    d={}
    call= slack_client.api_call("users.list")
    print (dir(call))
    users=call['members']
    for c in users:
        profile=c['profile']
        d[profile['real_name'].lower()]=c['name']
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



# if __name__== "__main__":
#     print fullnameNname()
