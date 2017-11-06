import slackapicall
import trellocall
import emailing
import time
from difflib import SequenceMatcher
def perform():
    mail=None
    duecards=trellocall.get_all_cards_with_duetime(24)
    participants=trellocall.project_team.get_members()
    d={}
    slack=slackapicall.nameNmail()
    for p in participants:
        #print dir(p)
        json_obj = trellocall.client.fetch_json('/members/' + p.id,query_params={'badges': False})
        print "bal",json_obj
        #print "trello",p.full_name.lower()
        d[p.id]=p.full_name.lower()
        
    #print d
    for c in duecards:
        message = "You have a task named \'"+c.name+"\' pending within today. You need to finish it ASAP and mark it complete by labelling green or archiving. Otherwise \
        I'll keep sending you mails every half an hour. :-) "
        members=c.member_ids
        for m in members:
            full_name=d[m]
            #print full_name
            key=None
            max=0
            for k in slack.keys():
                temp=SequenceMatcher(None,k,full_name).ratio()
                #print temp,k,full_name
                if temp>max:
                    max=temp
                    key=k
            mail=slack[key]
            #emailing.sendmail(mail,message)
            

    time.sleep(60*3)
            


if __name__=="__main__":
    perform()