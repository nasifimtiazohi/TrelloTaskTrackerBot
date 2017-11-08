from firebase import firebase
import pyrebase
import operator


config = {
  "apiKey": "AIzaSyCC5OzyEqGBcGZkpyUP90qUnyCCJY8SRQ8",
  "authDomain": "taskmangerbot.firebaseapp.com",
  "databaseURL": "https://taskmangerbot.firebaseio.com",
  "storageBucket": "taskmangerbot.appspot.com"
}

  # 1. Add all the cards of the user to the database
  # Nested DB structure:
  #+userid
  #-------total_points
  #------+card_id
  #--------------due_date(string)
  #--------------card_name (string)
  #--------------points (int)
  #--------------progress (string)

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

def add_card(due_date, card_name, progress, user_name, card_id):
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
  add_card("yhu22", "2017-10-25T16:00:00.000Z", 8, "test add card to firebase via python code", 50, "completed")

  Args:
      user (string): user id
      due_date (string): due date from trello card
      hours (int): number of hours to complete the task
      name (string): name of the card
      points (int): points reward for the task
      progress (string): progress of the task, "completed" or "pending"
  '''
  data = {"due_date": due_date, "card_name": card_name, "progress": progress}
  db.child("leaderboard/" + user_name + "/cards/"+ card_id).set(data)

def total_points_init():
  '''
  Initialize all member's total points
  '''
  all_users = db.child("leaderboard/").get()
  for user in all_users.each():
    db.child("leaderboard/" + user.key() + "/total_points").set(0)


def get_user_points(user):
  '''
  Get the total points from the user

  Example:
  get_total_points("guanxuyu")

  Args:
      user (string): user id
  '''
  # comment out the line below line to test the output value
  # print(db.child("leaderboard/" + user + "/total_points").get().val())
  return (db.child("leaderboard/" + user + "/total_points").get().val())

def store_total_points(performance):
  '''
  Store total points to the database

  Example:
  performance = {'gyu9': 10, 'yhu22': 20, 'xfu7': 30, 'simtiaz': 20, 'vinay638': 10}
  store_total_points(performance)


  Args:
    performance is a dict which keys are the user id and values are the total points

  '''
  for key, value in performance.iteritems():
    # new_total_points = {'total_points': value}
    db.child("leaderboard/" + key).update({'total_points': value})

# modify the value here to test
performance = {'gyu9': 15, 'yhu22': 25, 'xfu7': 30, 'simtiaz': 20, 'vinay638': 10}
# store_total_points(performance)

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

# print_leaderboard()
