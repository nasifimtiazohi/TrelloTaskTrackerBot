# Task Manager BOT #

Before running our code, please install some packages and setup the
environment variables, please see [Prerequisite](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service/src/README.md)

### Link to Screencast for SERVICE Milestone
[Screencast]()

### Files Related to SERVICE Milestone

**Platform**
1. Slack
1. Trello
1. Firebase 

File | Description
---  | ---
[CalculateGradePrinciples.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/master/CalculateGradePrinciples.md) | Reward Priciple that describes how we calculate the reward points and evaluate the difficulty of task
[Database Design](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/DatabaseDesign.md)| Display the structure of the our firebase database
[VM_README.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/VM_README.md) | The virtual machine we may use later as our server
[Worksheet-service.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/Worksheet-service.md)| Currently deprecated. Please refer to [Task Tracking](https://github.ncsu.edu/yhu22/CSC510_F17_Project/tree/service_submit#task-tracking)

src | Description
---  | ---
[db_helper.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service/src/db_helper.py) | Contains many helper functions deal with the firebase database
[emailing.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/emailing.py) | Helper to send nagging reminder
[envTest.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/envTest.py) | Test for environment variables setting
[main.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/main.py) | Integration of our three use cases and host of the BOT on Slack
[slackapicall.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/slackapicall.py) | Contains many helper functions deal with Slack channel and parser
[trellocall.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/trellocall.py) | Contains many helper functions parsing card information and list from Trello board
[usecase1.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/usecase1.py) | Implementation of use case 1
[usecase2.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/usecase2.py) | Implementation of use case 2
[usecase3.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/usecase3.py) | Implementation of use case 3
 
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
[Trello Task Manager](https://trello.com/b/MXYu6ZEy/task-manager-bot)  Used for task tracking like worksheet.

[Github Issues](https://github.ncsu.edu/yhu22/CSC510_F17_Project/issues) Issues to be solved for the implementation.

[Testing Board](https://trello.com/b/3L2DxAis/test-board) Trello board for us to test the function.

### Reference
1. https://api.slack.com/incoming-webhooks
2. https://github.com/thisbejim/Pyrebase
3. https://pypi.python.org/pypi/python-firebase/1.2
4. https://api.slack.com/rtm
5. https://github.com/slackapi/python-slackclient
