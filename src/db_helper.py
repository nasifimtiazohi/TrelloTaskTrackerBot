from firebase import firebase
import pyrebase
import trellocall
import operator
import os

# f = open("/home/ubuntu/dev/src/token.txt","r")
# token = []
# for l in f:
#   l=l.rstrip('\n')
#   token.append(l)

# apikey=token[7]
# authDomain=token[8]
# databaseURL=token[9]
# storageBucket=token[10]

# get Firebase API key, authDomain, databaseURL, storageBucket
apikey = os.getenv('FIREBASE_API_KEY')
authDomain= os.getenv('FIREBASE_AUTH_DOMAIN')
databaseURL= os.getenv('FIREBASE_DATABASE_URL')
storageBucket= os.getenv('FIREBASE_STORAGE_BUCKET')

config = {
  "apiKey": apikey,
  "authDomain": authDomain,
  "databaseURL": databaseURL,
  "storageBucket": storageBucket
}

# init the firebase config
firebase = pyrebase.initialize_app(config)

# get the db ref
db = firebase.database()

def get_all_info():
  '''
  Get all information from the leaderboard
  '''

  users = db.child("leaderboard").get()
  print(users.val())

# only call once at the beginning
def database_init():
  '''
  Initialize the data in firebase and sync the data in trello board

  card_info[0]= due_date
  card_info[1]= card_name
  card_info[2]= progress
  card_info[3] = user_name list
  card_info[4] = card_id
  '''
  # Init Firebase database everyday
  all_card_info = []
  all_card_info = trellocall.get_all_cards()
  for card_info in all_card_info:
    print "card info",type(card_info)
    if card_info[2] == "Completed":
      add_card(str(card_info[0]), str(card_info[1]), str(card_info[2]), card_info[3], str(card_info[4]), "true")
    elif card_info[2] == "Pending":
      add_card(str(card_info[0]), str(card_info[1]), str(card_info[2]), card_info[3], str(card_info[4]), "false")

def update_progres(trello_username, card_id):
  '''
  Update the card progress according to the user

  Example:
  update_progres("otto292", "59eb634b9c84cc02182a487b")

  Args:
      trello_username (string): user id in trello
      card_id (string): trello card id
  '''
  # update card progress
  db.child("leaderboard/" + trello_username+ "/cards/" + card_id).update({'progress': "Completed"})

def reward_points(trello_username, points):
  '''
  Give certain reward points to a user who completes the assigned task

  Example:
  reward_points("otto292", 20)

  Args:
      trello_username (string): user id in trello
      points (int): reward points
  '''
  # reward points
  total = get_user_points(trello_username) + points
  db.child("leaderboard/" + trello_username).update({'total_points': total})

def sync_card_info():
  '''
  Synchronize the information between trello board and firebase database
  '''
  all_card_info = []
  all_card_info = trellocall.get_all_cards()
  for card_info in all_card_info:
    # detect if there are new cards, if no,
    data = {"due_date": str(card_info[0]), "card_name": str(card_info[1]), "progress": str(card_info[2])}
    for names in card_info[3]:
      db.child("leaderboard/" + str(names) + "/cards/"+ str(card_info[4])).update(data)


def add_card(due_date, card_name, progress, user_name_list, card_id, is_congrats):
  '''
  Add card to certain member in firebase database
      card_info[0]= due_date
      card_info[1]= card_name
      card_info[2]= progress
      card_info[3] = user_name
      card_info[4] = card_id
      card_info[5] = is_congrats

  Example:
  add_card("2017-10-25T16:00:00.000Z", "test add card to firebase via python code", "completed", "otto292", "59eba737418e777a4ac31360", "false")

  Args:
      due_date (string): due date from trello card
      card_name (string): name of the card
      progress (string): progress of the task, "completed" or "pending"
      user_name (string): user id
      card_id (string): card id
      is_congrats (string): has been post congrats message or not
  '''
  print type(user_name_list),user_name_list
  for user_name in user_name_list:
    print user_name
    data = {"due_date": due_date, "card_name": card_name, "progress": progress, "is_congrats": is_congrats}
    db.child("leaderboard/" + str(user_name) + "/cards/"+ card_id).set(data)

def total_points_init():
  '''
  Initialize all member's total points in firebase database
  '''
  all_users = db.child("leaderboard/").get()
  for user in all_users.each():
    db.child("leaderboard/" + user.key() + "/total_points").set(0)

# This function search in firebase database using cardname and return the card id
def getCardIdbyCardName(user, cardname):
  '''
  Search the card by card id for certain user in firebase database

  Example:
  getCardIdbyCardName("otto292", "Create Mocking data")

  Args:
      user (string): user id
      cardname (string): card name in firebase database as well as card name on trello board
  '''
  # retrieve parent key by child value
  cards = db.child("leaderboard/" + user + "/cards").get()
  for card in cards.each():
    card_name_in_db = str(db.child("leaderboard/" + user + "/cards/"+ card.key()+ "/card_name").get().val())
    card_name_in_db = card_name_in_db.strip().lower()
    if card_name_in_db == cardname.strip().lower():
      return card.key()

def update_congratualtion_status(user, card_id):
  '''
  Update the status of card that already posted congratulation message

  Example:
  update_congratualtion_status("otto292", "59eb634b9c84cc02182a487b")

  Args:
      user (string): user id
      card_id (string): card id
  '''
  db.child("leaderboard/" + user + "/cards/" + card_id).update({'is_congrats': "true"})

def check_if_done(user, card_id):
  '''
  Check if the card already posted congratulation message message

  Example:
  check_if_done("otto292", "59eb634b9c84cc02182a487b")

  Args:
      user (string): user id
      card_id (string): card id
  '''
  return (db.child("leaderboard/" + user + "/cards/" + card_id +"/is_congrats").get().val())

def get_progress_of_card(user, card_id):
  '''
  Get the progress of the card, return "Completed" or "Pending"

  get_progress_of_card("otto292", "59eb634b9c84cc02182a487b")

  Args:
      user (string): user id
      card_id (string): card id
  '''
  return (db.child("leaderboard/" + user + "/cards/" + card_id + "/progress").get().val())

def add_field_to_allusers(field, value):
  '''
  Add customized field to a card for all users

  Example:
  add_field_to_allusers("is_congrats", "false")

  Args:
      field (string): new field of card
      value: depends on field type
  '''
  all_users = db.child("leaderboard/").get()
  for user in all_users.each():
    db.child("leaderboard/" + user.key()).update({field: value})

#add_field_to_allusers("target_points", 100)

def get_user_points(user):
  '''
  Get the total points from the user

  Example:
  get_total_points("guanxuyu")

  Args:
      user (string): user id
  '''
  return (db.child("leaderboard/" + user + "/total_points").get().val())

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

# modify the value here to test sotre_total_points function
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
