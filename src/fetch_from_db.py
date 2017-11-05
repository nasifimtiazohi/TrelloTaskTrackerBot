from firebase import firebase
import pyrebase

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

def add_card(user, due_date, hours, name, points, progress):
  '''
  Add card to certain member

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

  data = {"check_list": {"test add card": 0}, "due_date": due_date, "hours": hours, "name": name, "points": points, "progress": progress}
  member = db.child("leaderboard/" + user + "/cards").push(data)

def get_total_points(user):
  '''
  Get the total points from the user

  Example:
  get_total_points("yhu22")

  Args:
      user (string): user id
  '''
  # comment out the line below line to test the output value
  # print(db.child("leaderboard/" + user + "/total_points").get().val())
  return (db.child("leaderboard/" + user + "/total_points").get().val())
