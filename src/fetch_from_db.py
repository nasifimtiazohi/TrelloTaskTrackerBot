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

# firebase = firebase.FirebaseApplication('https://taskmangerbot.firebaseio.com/leaderboard/')
# point = firebase.get('gyu9', '/Card1')
# print(users)

# get the db ref
db = firebase.database()
# get all users from the leaderboard
users = db.child("leaderboard").get()
print(users.val())
