import slackapicall
import trellocall
import emailing
import time
from difflib import SequenceMatcher
def mainFlow(threadName, delay):
    print "ashche"
    automaetd ="\n\n This is an automated message. Replying has no value to it."
    while True:
        #mainflow start
        mail=None
        duecards=trellocall.get_all_cards_for_usecase1()
        participants=trellocall.project_team.get_members()
        d={}
        slack=slackapicall.nameNmail()

        for p in participants:
            json_obj = trellocall.client.fetch_json('/members/' + p.id,query_params={'badges': False})
            d[p.id]=p.full_name.lower()
            
        for c in duecards[0]:
            message = "You have a task named \'"+c.name+"\' pending within 12 hours. You need to finish it ASAP and mark it complete by labelling green or archiving.\
 Otherwise I'll keep sending you mails every half an hour. :-) "
            message+=automaetd
            members=c.member_ids

            for m in members:
                full_name=d[m]
                print full_name
                key=None
                max=0
                for k in slack.keys():
                    temp=SequenceMatcher(None,k,full_name).ratio()
                    #print temp,k,full_name
                    if temp>max:
                        max=temp
                        key=k
                mail=slack[key]
                emailing.sendmail(mail,message)
        for c in duecards[1]:
            message = "You have a \'moderately difficult\' task named \'"+c.name+"\' pending within 24 hours. You need to finish it ASAP and mark it complete by labelling green or archiving.\
Also, you can remove the label \'Medium\' and change the label to \'Easy\' to stop getting mails for another 12 hours. Otherwise I'll keep sending you mails every half an hour. :-) "
            message+=automaetd
            members=c.member_ids

            for m in members:
                full_name=d[m]
                print full_name
                key=None
                max=0
                for k in slack.keys():
                    temp=SequenceMatcher(None,k,full_name).ratio()
                    #print temp,k,full_name
                    if temp>max:
                        max=temp
                        key=k
                mail=slack[key]
                emailing.sendmail(mail,message)
        for c in duecards[2]:
            message = "You have a \'Hard\' task named \'"+c.name+"\' pending within 36 hours. You need to finish it ASAP and mark it complete by labelling green or archiving.\
Also, you can remove the label \'Hard\' and change the label to \'Medium\' or \'Easy\' to stop getting mail for another 12 or 24 hourse respectively. Otherwise I'll keep sending you mails every half an hour. :-) "
            message+=automaetd
            members=c.member_ids

            for m in members:
                full_name=d[m]
                print full_name
                key=None
                max=0
                for k in slack.keys():
                    temp=SequenceMatcher(None,k,full_name).ratio()
                    #print temp,k,full_name
                    if temp>max:
                        max=temp
                        key=k
                mail=slack[key]
                emailing.sendmail(mail,message)        
        time.sleep(delay)  

def alternateFlow(threadName,delay):
    while True:
        automaetd ="\n\n This is an automated message. Replying has no value to it."
        mail=None
        participants=trellocall.project_team.get_members()
        d={}
        slack=slackapicall.nameNmail()

        for p in participants:
            json_obj = trellocall.client.fetch_json('/members/' + p.id,query_params={'badges': False})
            d[p.id]=p.full_name.lower()
        final=trellocall.get_cards_for_UC1_alternate()
        for c in final:
            message = "For card, \'"+c.name+"\', You don't have either due_date or difficulty labels (yellow for easy, sky for medium, black for hard) set. Please set them in trello, otherwise I'll keep sending you email every 12 hours."
            message+=automaetd
            members=c.member_ids

            for m in members:
                full_name=d[m]
                print full_name
                key=None
                max=0
                for k in slack.keys():
                    temp=SequenceMatcher(None,k,full_name).ratio()
                    #print temp,k,full_name
                    if temp>max:
                        max=temp
                        key=k
                mail=slack[key]
                emailing.sendmail(mail,message)        
        time.sleep(delay)        

if __name__=="__main__":
    print "something"