from firebase import firebase
import pyrebase
import trellocall
import operator
# import trellocall


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


def get_all_info():
  '''
  Get all information from the leaderboard

  Example:
  get_all_info()
  '''

  users = db.child("leaderboard").get()
  print(users.val())

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
  all_card_info = trellocall.get_all_cards()
  for card_info in all_card_info:
    # detect if there are new cards
    add_card(card_info[0], card_info[1], card_info[2], card_info[3], card_info[4], "false")


def update_progres(trello_username, card_id):
   #update progress
   db.child("leaderboard/" + trello_username+ "/cards/" + card_id).update({'progress': "Completed"})

def reward_points(trello_username, points):
 # reward points
 # TypeError: unsupported operand type(s) for +: 'NoneType' and 'int'
  total = get_user_points(trello_username) + points
  print total
  db.child("leaderboard/" + trello_username).update({'total_points':total })
    
def add_card(due_date, card_name, progress, user_name, card_id, is_congrats):
  '''
  Add card to certain member
                    card_info[0]= due_date
                    card_info[1]= card_name
                    card_info[2]= 20
                    card_info[3]= progress
                    card_info[4] = user_name
                    card_info[5] = card_id
                    card_info[6] = userid

  Example:
  add_card("yhu22", "2017-10-25T16:00:00.000Z", 8, "test add card to firebase via python code", 50, "completed", "False")

  Args:
      user (string): user id
      due_date (string): due date from trello card
      hours (int): number of hours to complete the task
      name (string): name of the card
      points (int): points reward for the task
      progress (string): progress of the task, "completed" or "pending"
      is_congrats (boolean): has been post congrats message or not
  '''
  data = {"due_date": due_date, "card_name": card_name, "progress": progress, "is_congrats": is_congrats}
  db.child("leaderboard/" + user_name + "/cards/"+ card_id).set(data)

def total_points_init():
  '''
  Initialize all member's total points
  '''
  all_users = db.child("leaderboard/").get()
  for user in all_users.each():
    db.child("leaderboard/" + user.key() + "/total_points").set(0)

#################################################################################################################

# This function search in firebase database using cardname and return the card id 

#################################################################################################################
def getCardIdbyCardName(user, cardname):
  # retrieve parent key by child value
  cards = db.child("leaderboard/" + user + "/cards").get()
  for card in cards.each():
    card_name_in_db = db.child("leaderboard/" + user + "/cards/"+ card.key()+ "/card_name").get().val()
    card_name_in_db = card_name_in_db.strip().lower()
    if card_name_in_db == cardname.strip().lower():
      return card.key()
  
def update_congratualtion_status(user, card_id):
  db.child("leaderboard/" + user + "/cards/" + card_id).update({'is_congrats': "true"})

def check_if_done(user, card_id):
  return (db.child("leaderboard/" + user + "/cards/" + card_id +"/is_congrats").get().val())
def get_progress_of_card(user, card_id):

  return (db.child("leaderboard/" + user + "/cards/" + card_id + "/progress").get().val())

def get_user_points(user):
  '''
  Get the total points from the user

  Example:
  get_total_points("guanxuyu")

  Args:
      user (string): user id
  '''
  # comment out the line below line to test the output value
  #print(db.child("leaderboard/" + user + "/total_points").get().val())
  points = db.child("leaderboard/" + user + "/total_points").get().val()
  return points

def get_user_target_points(user):
  '''
  Get the target points from the user

  Example:
  get_target_points("guanxuyu")

  Args:
      user (string): user id
  '''
  # comment out the line below line to test the output value
  # print(db.child("leaderboard/" + user + "/total_points").get().val())
  return (db.child("leaderboard/" + user + "/target_points").get().val())

def store_total_points(performance):
  '''
  Store total points to the database
  Example:
  performance = {'guanxuyu': 15, 'otto292': 25, 'xiaotingfu1': 30, 'sheikhnasifimtiaz': 20, 'vinay638': 10}
  store_total_points(performance)
  Args:
    performance is a dict which keys are the user id and values are the total points

  '''
  for key, value in performance.iteritems():
    # new_total_points = {'total_points': value}
    db.child("leaderboard/" + key).update({'total_points': value})

# modify the value here to test
# performance = {'guanxuyu': 15, 'otto292': 25, 'xiaotingfu1': 30, 'sheikhnasifimtiaz': 20, 'vinay638': 10}
# store_total_points(performance)

def store_target_points(targets):
  '''
  Store total points to the database

  Example:
  targets = {'guanxuyu': 15, 'otto292': 25, 'xiaotingfu1': 30, 'sheikhnasifimtiaz': 20, 'vinay638': 10}
  store_total_points(performance)


  Args:
    targest is a dict which keys are the user id and values are the total points

  '''
  for key, value in targets.iteritems():
    # new_total_points = {'total_points': value}
    db.child("leaderboard/" + key).update({'target_points': value})


def update_card_progress(user, card_id, progress):
  '''
  Update card progress for user's card

  Example:
  update_card_progress("otto292", "59eb634b9c84cc02182a487b", "Completed")

  Args:
    user (string): user_id
    card_id (string): card id
    progress (string): either "Pending" or "Completed"
  '''
  db.child("leaderboard/" + user + "/cards/" + card_id).update({'progress': progress})

def add_field_to_card(user, card_id, field, value):
  '''
  Add field to a card in database

  Example:
  add_field_to_card("otto292", "59eb634b9c84cc02182a487b", "done", False)

  Args:
    user (string): user_id
    card_id (string): card id
    field (string): new field
    value (type depends): value of the new field
  '''
  db.child("leaderboard/" + user + "/cards/" + card_id).update({field: value})

def set_field_value_of_card(user, card_id, field, value):
  '''
  Set the value of field to a card in database

  Example:
  set_field_value_of_card("otto292", "59eb634b9c84cc02182a487b", "done", True)

  Args:
    user (string): user_id
    card_id (string): card id
    field (string): new field
    value (type depends): value of the new field
  '''
  db.child("leaderboard/" + user + "/cards/" + card_id + "/" + field).set(value)

def add_field_to_allcards(field, value):
  '''
  Add the new field with certain value to all cards

  Example:
  add_field_to_allcards("done", False)

  Args:
    field (string): new field
    value (type depends): value of the new field
  '''
  all_users = db.child("leaderboard/").get()
  for user in all_users.each():
    all_cards = db.child("leaderboard/" + user.key() + "/cards/").get()
    for card in all_cards.each():
      db.child("leaderboard/" + user.key() + "/cards/" + card.key()).update({field: value})

def set_field_value_of_allcards(field, value):
  '''
  Apply the same change of one field of card to all cards

  Example:
  set_field_value_of_allcards("done", True)

  Args:
    field (string): new field
    value (type depends): value of the new field
  '''
  all_users = db.child("leaderboard/").get()
  for user in all_users.each():
    all_cards = db.child("leaderboard/" + user.key() + "/cards/").get()
    for card in all_cards.each():
      db.child("leaderboard/" + user.key() + "/cards/" + card.key() + "/" + field).set(value)

def print_leaderboard():
  '''
  Print each user's total points

  Example:
  print_leaderboard()
  '''
  all_users = db.child("leaderboard/").get()
  leaderboard = {}

  for user in all_users.each():
    leaderboard[user.key()] = db.child("leaderboard/" + user.key() + "/total_points").get().val()

  sorted_leaderboard = sorted(leaderboard.items(), key=operator.itemgetter(1), reverse=True)
  print(sorted_leaderboard) # change print to return for later use to export to trello platform

#reward_points("xiaotingfu1", 50)
#print_leaderboard()
#print getCardIdbyCardName("xiaotingfu1", ' fix bugs for use case 3')
