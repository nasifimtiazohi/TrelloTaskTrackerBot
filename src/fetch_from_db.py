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

# get all users from the leaderboard
def get_all_info():
  users = db.child("leaderboard").get()
  print(users.val())

def add_card(user, due_date, hours, name, points, progress):
  data = {"check_list": {"test add card": 0}, "due_date": due_date, "hours": hours, "name": name, "points": points, "progress": progress}
  member = db.child("leaderboard/" + user + "/cards").push(data)

add_card("gyu9", "tomorrow", 8, "add card to firebase", 50, "pending")

#get_all_info()
