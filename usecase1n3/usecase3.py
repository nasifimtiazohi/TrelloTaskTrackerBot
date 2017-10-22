import slackapicall
import trellocall

def perform():
    users=trellocall.slackname_with_duecards()
    dm_channel=[]
    for u in users:
        #print slackapicall.name_to_id(u)
        userid=slackapicall.name_to_id(u)
        l=[]
        channel=slackapicall.open_im(userid)
        print u,userid,channel
        l.extend((userid,u,channel))
        dm_channel.append(l)
    return dm_channel

if __name__=="__main__":
    perform()
