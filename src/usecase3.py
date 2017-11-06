import slackapicall
import trellocall
from firebase import firebase
import pyrebase
from datetime import datetime

'''
  Use Case 3: 

      S1: The bot will ask for progress to each member based on his tasks and due dates.
      S2: It will wait a certain period (differing on scenario, periods will be dynamically calculated).
      S3: If response is positive (response of progress), 
      it will post congratulatory message on a public channel and award score in the leaderboard.
      S4: If response is negative (either no response/response of no progress), (we assum our user is honest)
      it will post reminder message to a public channel and add penalties in his score in the leaderboard.

      Alternative flow:
      A1: 1.If information is missing about any member, it will post message to public channel that the member is inactive.

   Implementation:
   Don't need to type "Use Case 3" command to retrieve data!
   Run the bot and fetch data from trello 
'''

def reward_points():
  '''
  Reward points according to rewarding principles
  Save points to database under each person's name

  Args:
      
  '''    

    

def post_public_message():
  '''
    Post the message to the general channel

  Args:
      
  '''   

def check_progress():
  '''
  Check progress of each member's progress twice a day:
  7:00 AM and 11:00 PM

  This function should be always running and monitoring the progress
  This function can be triggered by a time event

  Example:
  perform()

  Args:
      
  '''
  #For each user who have cards check progress
  #namelist_with_duecards=get_all_cards_with_duedate()
  #get the uid of user who has task pending within 48 hours
  #get uid

  users_with_cards=trellocall.slackname_with_duetime(48)
  dm_channel=[]
  for u in users_with_cards.keys():
        #message= u
        #get uid
        #print slackapicall.name_to_id(u)
        userid=slackapicall.name_to_id(u)
        cardlist=users_with_cards[u] 
        message=u+" ," +"you have "+ str(len(cardlist)) + " task pending that approach the due"
        i = 0
        for card in cardlist: 
            i+=1
            message+=". Task "+ str(i) +": "+ card.name+" ,please update your progress for this card here: " + "https://taskmangerbot.firebaseapp.com"+ "?userid=" + u + "&card_id="+card.id 
            print message
            print card.id
        l=[]
        channel=slackapicall.open_im(userid)
        #print u,userid,channel
        l.extend((userid,u,channel,cardlist,message))
        dm_channel.append(l)
  return dm_channel


  
def calculate_time_period():
  '''
  Check progress of each member's progress twich a day:
  7:00 AM and 11:00 PM
  This function should be always running and monitoring the progress
  This function can be triggered by a time event

  Example:
  perform()

  Args:     
  '''

if __name__=="__main__":
    d = check_progress()
    #print d
