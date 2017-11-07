# Task Manager BOT #

Note: The MILESTONE: SERVICE should refer to **service** branch.

Before running our code, please install some packages below:

*py-trello*
```
pip install py-trello
```

*pyrebase*
```
pip install pyrebase
```
*python-firebase 1.2*
```
sudo pip install python-firebase
```


### Link to Screencast for SERVICE Milestone
[Screencast]()

### Files Related to BOT Milestone

File | Description
---  | ---


### Group Members

Name | Unity ID 
--- | --- 
Xiaoting Fu | xfu7
Vinay Gupta | vgupta8
Nasif Imtiaz | simtiaz
Yu-Ching Hu | yhu22
Guanxu Yu | gyu9

## Milestone - SERVICE ##
Our bot runs on the assumption that a team will have their workspace both on "Slack" and "Trello". They use trello to keep track of their tasks, and "Slack" for communication. With necessary permissions, our bot resides in Slack and also can fetch/post data on Trello workspace of the team. 


### Task Tracking
[Trello Task Manager](https://trello.com/b/MXYu6ZEy/task-manager-bot)

[Testing Board](https://trello.com/b/3L2DxAis/test-board)

### Reference
https://api.slack.com/incoming-webhooks
https://github.com/thisbejim/Pyrebase
https://pypi.python.org/pypi/python-firebase/1.2
https://api.slack.com/rtm

**You cannot provide attachments nor buttons to messages posted over the RTM API.
If your bot user needs to send more complex messages, use the web API's chat.postMessage or chat.postEphemeral.**
