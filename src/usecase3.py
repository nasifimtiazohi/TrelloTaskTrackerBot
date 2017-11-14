import slackapicall
import trellocall
from firebase import firebase
import pyrebase
from datetime import datetime

#################################################################################################################
#                                                     Use Case 3                                                #
#
#      S1: The bot will ask for progress to each member based on his tasks and due dates.
#      S2: It will wait a certain period (differing on scenario, periods will be dynamically calculated).
#      S3: If response is positive (response of progress),
#      it will post congratulatory message on a public channel and award score in the leaderboard.
#      S4: If response is negative (either no response/response of no progress), (we assum our user is honest)
#      it will post reminder message to a public channel and add penalties in his score in the leaderboard.
#
#      Alternative flow:
#      A1: 1.If information is missing about any member,
#       it will post message to public channel that the member is inactive.                                     #
#################################################################################################################
#
#   Implementation:
#     This python scripts does run by itself, it is designed to be called by the main.py function and perform tasks
#     related to the requirements of use case 3
#
#   Function:
#
#    post_public_message():
#
#################################################################################################################


################################################################################################################
# Function:
# name:
#       check_progress() : keep track of user progress and send message to ask for their input
#       sspost_public_message(): post message to slack in response to user input
#
# return:
#         dm_channel: list of
#                              userid: trello user id
#                              u: email id i.e. xfu7
#                              channel: direct message channel
#                              cardlist: list of due cards of this user
#                              message: target message to send to the channel
# Implementations:
#   Post the message to the general channel
#   Check in the progress in the task list, if the progress is "Completed", post a message to the user
#
################################################################################################################

def post_public_message():
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

################################################################################################################
# Function:
# name:
#         check_progress()
# return:
#         dm_channel: list of
#                              userid: trello user id
#                              slack_name: email id i.e. xfu7
#                              channel: direct message channel
#                              cardlist: list of due cards of this user
#                              message: target message to send to the channel
# Implementations:
#   Check progress of each member's progress every 3 minutes if user has card pending within 8 hours
#   If user complete the task, we will do the following things
#     1. We will update his progress (="completed") in database and also update the points to his total points (reward)
#     2. We will update trello, mark the card as DONE automatically
#     3. we will send congraculation message in public channel, so user's teammate can find their motivation of working harder
#   If user ignore our reminder, or he provide an negative reponse,
#     we will do the following things:
#     1. We will update his progress (="pending")in database and also update the points to his total points (penality)
#     2. Keep sending the reminder
################################################################################################################
def check_progress():

  #we are using trello_user_name
  users_with_cards=trellocall.slackname_with_duetime(20)
  dm_channel=[]
  # u is the slack_id, e.g. xfu7
  for slack_name in users_with_cards.keys():
        #userid: slack user id
        userid=slackapicall.fullname_to_id(slack_name)
        cardlist=users_with_cards[slack_name]
        message= "<@"+userid+"> ," +" you have "+ str(len(cardlist)) + " task pending that approach the due"
        i = 0
        for card in cardlist:
            i+=1
            message+=". Task "+ str(i) +": "+ card.name+" ,please respond your status of completeness AND the name of the task: @taskbot YOUR STATUS, YOUR TASK Name, separated using ' , ' sysmbol. e.g: Completed, Task 1"
        l=[]
        channel=slackapicall.open_im(userid)
        l.extend((userid,slack_name,channel,cardlist,message))
        dm_channel.append(l)
  return dm_channel
