import slackapicall
import trellocall
from firebase import firebase
import pyrebase
from datetime import datetime
from db_helper import get_user_points, add_card

''' nasif:
  1. why do we initialize database everytime? Because our trello card may change everyday.
  2. Are we not penalizing points and posting shame message on general channel? '''

''' Xiaoting:
  Fix problems in UC3,
  1. reply to individual person, instad of all
  2. after replying to each person, update the trello card and also database information
  3. Post Congratulation message, penality message'''


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
#print "The performance point: " + str(trellocall.getPerformancePoints())
#init list of all cards
'''
                    card_info[0]= due_date
                    card_info[1]= card_name
                    card_info[2]= progress
                    card_info[3] = user_name
                    card_info[4] = card_id

'''

def database_init():
  # Init Firebase database everyday
  all_card_info = []
  all_card_info = trellocall.get_all_cards_of_user()
  for card_info in all_card_info:
    add_card(card_info[0], card_info[1], card_info[2], card_info[3], card_info[4], False)

# If user complete the task, we will add points for this user and then update his performance point

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
  update trello label from red to green

  Example:
  reward_points("yhu22", 50)

  Args:
        user (string): user id
        points (int): points reward for the task

  '''
  # print("Before adding reward points: ",get_user_points(user))
  db.child("leaderboard/" + user).update({'total_points': (get_user_points(user) + points)})

  users_with_cards=trellocall.slackname_with_duetime(20)

  for u in users_with_cards.keys():
        #get uid
        userid=slackapicall.fullname_to_id(u)
        cardlist=users_with_cards[u]
        #trellocall.completeCards(card_id, cardlist)
        for card in cardlist:
          #TODO: user with multiple cards
           trellocall.update_progress(user, card)
  # print("After adding reward points: ",get_user_points(user))

def post_public_message():
  '''
    Post the message to the general channel
    Check in the progress in the task list, if the progress is "Completed", post a message to the user

  Args:
  '''
  #if the user finish the task, says congratulations to him
  users_with_cards=trellocall.slackname_with_duetime(20) #this function is returning due cards.. How do you measure if they are finished?
  dm_channel=[]
  for u in users_with_cards.keys():
        #get uid
        userid=slackapicall.fullname_to_id(u)
        cardlist=users_with_cards[u]
        message="Congratulations to <@"+ userid+"> ," +" for finishing the task before the deadline!"
        l=[]
        channel=slackapicall.open_im(userid)
        #print u,userid,channel
        l.extend((userid,u,channel,cardlist,message))
        dm_channel.append(l)
  return dm_channel

def check_progress():
  '''
  default progress is pending
  Check progress of each member's progress every 3 minutes if user has card pending within 8 hours
  If user complete the task, we will do the following things:
  1. We will update his progress (="completed") in database and also update the points to his total points (reward)
  2. We will update trello, mark the card as DONE automatically
  3. we will send congraculation message in public channel, so user's teammate can find their motivation of working harder

  If user ignore our reminder, or he provide an negative reponse,
  we will do the following things:
  1. We will update his progress (="pending")in database and also update the points to his total points (penality)
  2. Keep sending the reminder

  Example:
  check_progress()
  Args:
  '''
  #we are using trello_user_name
  users_with_cards=trellocall.slackname_with_duetime(20)
  dm_channel=[]
  # u is the slack_id, e.g. xfu7
  for slack_name in users_with_cards.keys():

        print "People with due cards"+ slack_name
        userid=slackapicall.fullname_to_id(slack_name)
        cardlist=users_with_cards[slack_name]
        ''' no need to match with trello name. slack name is fine '''
        # #mapping from slack_id to trello_user_name, full_name
        # trello_user_name = trellocall.slack_name_to_trello_name(slack_name)
        # #print trello_user_name
        message= "<@"+userid+"> ," +" you have "+ str(len(cardlist)) + " task pending that approach the due"
        i = 0
        for card in cardlist:
            i+=1
            message+=". Task "+ str(i) +": "+ card.name+" ,please respond your status of completeness AND the name of the task: @taskbot YOUR STATUS, YOUR TASK"
        l=[]
        channel=slackapicall.open_im(userid)
        #print u,userid,channel
        l.extend((userid,slack_name,channel,cardlist,message))
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
    # database_init()
    print d
