import slackapicall
import trellocall
from firebase import firebase
import pyrebase
from datetime import datetime
from fetch_from_db import get_user_points, add_card

config = {
  "apiKey": "AIzaSyCC5OzyEqGBcGZkpyUP90qUnyCCJY8SRQ8",
  "authDomain": "taskmangerbot.firebaseapp.com",
  "databaseURL": "https://taskmangerbot.firebaseio.com",
  "storageBucket": "taskmangerbot.appspot.com"
}

# init the firebase config
firebase = pyrebase.initialize_app(config)
# get the db ref
db = firebase.database()
#init list of all cards
'''
                    card_info[0]= due_date
                    card_info[1]= card_name
                    card_info[2]= 20
                    card_info[3]= progress
                    card_info[4] = user_name
                    card_info[5] = card_id
                    card_info[6] = userid
'''

def database_init():
  # Init Firebase database everytime
  all_card_info = []
  all_card_info = trellocall.get_all_cards_of_user()
  for card_info in all_card_info:
    print card_info
    add_card(card_info[0], card_info[1], card_info[2], card_info[3], card_info[4], card_info[5])

'''
Fetch data from trello and store it into database
Find all the cards of each user
'''

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

def reward_points(user, points):
  '''
  Reward points according to rewarding principles
  Save points to database under each person's name

  Example:
  reward_points("yhu22", 50)

  Args:
        user (string): user id
        points (int): points reward for the task

  '''
  # print("Before adding reward points: ",get_user_points(user))
  db.child("leaderboard/" + user).update({'total_points': (get_user_points(user) + points)})
  # print("After adding reward points: ",get_user_points(user))

def post_public_message():
  '''
    Post the message to the general channel
    Check in the progress in the task list, if the progress is "Completed", post a message to the user

  Args:
  '''
  
  #if the user finish the task, says congratulations to him
  users_with_cards=trellocall.slackname_with_duetime(48)
  dm_channel=[]
  for u in users_with_cards.keys():
        #get uid
        userid=slackapicall.name_to_id(u)
        cardlist=users_with_cards[u]
        message="Congratulations! "+u+" ," +" has finished the task before the deadline!"
        l=[]
        channel=slackapicall.open_im(userid)
        #print u,userid,channel
        l.extend((userid,u,channel,cardlist,message))
        dm_channel.append(l)
  return dm_channel

def check_progress():
  '''
  Check progress of each member's progress twice a day: 7:00 AM and 11:00 PM
  This function should be always running and monitoring the progress
  This function can be triggered by a time event
  Example:
  check_progress()
  Args:
  '''
  #we are using trello_user_name
  users_with_cards=trellocall.slackname_with_duetime(48)
  dm_channel=[]
  # u is the slack_id, e.g. xfu7
  for slack_name in users_with_cards.keys():
        #message= u
        #get uid
        #print slackapicall.name_to_id(u)
        userid=slackapicall.name_to_id(slack_name)
        cardlist=users_with_cards[slack_name]
        #mapping from slack_id to trello_user_name, full_name
        trello_user_name = trellocall.slack_name_to_trello_name(slack_name)
        #print trello_user_name   
        message= trello_user_name+" ," +"you have "+ str(len(cardlist)) + " task pending that approach the due"
        i = 0
        for card in cardlist:
            i+=1
            message+=". Task "+ str(i) +": "+ card.name+" ,please update your progress for this card here: " + "https://taskmangerbot.firebaseapp.com"+ "?userid=" + trello_user_name + "&card_id="+card.id 
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

  Args:     
  '''

if __name__=="__main__":
    d = check_progress()
    #print d
