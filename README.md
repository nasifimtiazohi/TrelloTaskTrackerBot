# Task Manager BOT #

Before running our code, please install some packages and setup the
environment variables, please see [Prerequisite](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service/src/README.md)

### Link to Screencast for SERVICE Milestone
[Intro](https://drive.google.com/file/d/1LtsbSFsaZhQ-AYc5esdJFXA481XKAjUg/view?ts=5a0bc35d)

[Usecase 1](https://drive.google.com/a/ncsu.edu/file/d/1cE1X2B7SnvV0PbFdlXffycbGe6KrWbS_/view?usp=sharing)

[Usecase 2](https://drive.google.com/a/ncsu.edu/file/d/10HoRUdvbmN8EQuk4mZbvEdt7d8rGOHex/view?usp=sharing)

[Usecase 3](https://drive.google.com/file/d/14tf-NjdPnLB-tfzBrNn3XOXR0Wj_y1Sb/view?ts=5a0bc375)

### Files Related to SERVICE Milestone

Platform |
--- |
Slack |
Trello |
Firebase | 

File | Description
---  | ---
[CalculateGradePrinciples.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/master/CalculateGradePrinciples.md) | Reward Priciple that describes how we calculate the reward points and evaluate the difficulty of task
[Database Design](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/DatabaseDesign.md)| Display the structure of the our firebase database
[VM_README.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/VM_README.md) | The virtual machine we may use later as our server
[Worksheet-service.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/Worksheet-service.md)| Currently deprecated. Please refer to [Task Tracking](https://github.ncsu.edu/yhu22/CSC510_F17_Project/tree/service_submit#task-tracking)

src | Description
---  | ---
[main.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/main.py) | Integration of our three use cases and host of the BOT on Slack
[db_helper.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service/src/db_helper.py) | Contains many helper functions deal with the firebase database
[slackapicall.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/slackapicall.py) | Contains many helper functions deal with Slack channel and parser
[trellocall.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/trellocall.py) | Contains many helper functions parsing card information and list from Trello board
[envTest.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/envTest.py) | Test for environment variables setting
[emailing.py](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/service_submit/src/emailing.py) | Helper to send nagging reminder
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

### Methodology

When user creates a card, we make it a rule that **Label** of a card stands for the progress or difficulty of a task.

e.g. Green Label(Done), Red Label(To Do) / Yellow Label(Easy), Blue Label(Median), Black Label(Hard)
Full rules and condition described in [CalculateGradePrinciples.md](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/master/CalculateGradePrinciples.md)

Once a task was assigned, the BOT will send reminder to the assignee and ask for the progress in a certain time interval. If the assignee did not response, the BOT will keep sending reminder.
According to the different difficulty of task, we will give corresponding reward points once the assignee completed his/her work or deduct points if job did not complete. Besides, there is a leader board that records each member's performance. (i.e. points) We also have individual target board for each member to improve their productivty.

For the interaction between user and the BOT on Slack. We make some rule for the BOT to parse user's command.
For example, in order for our BOT to recognize their command they should use the following format:
@taskbot done > Task 1 (the name of the task).

The name of the task will be printed by the BOT to remind the user.

Here, 'done' is considered as positive response. There are some other positive response words, such as 'finished', 'completed', "i'm done", "yes", "of course", "i finished", "yep", "1".

As for negative words, for example: 'pending', '0', 'not yet', 'incomplete', 'wait', 'almost', 'no', 'nah', "i haven't"


### Use Case
1. Send Nagging Reminder 
```  
    Precondition: User must give the due date and optionally expected hours for completion when adding a new task to the list. The user optionally is expected to update the progress of the task also.
 
    Main Flow: Bot will track the timeline of the task and progress [S1]. If it’s necessary, it will send reminders [S2]. It can continuously send reminders until the user takes action [S3].

    Subflows:
    S1: Bot would have a logic system to calculate checkpoints. (e.g., 2 days before the due date if the task has 6 hours of equivalent work remained incomplete)
    S2: It will send notifications to the user. ( e.g. send an email to user)
    S3: It will wait for a certain amount of time for the user’s response. In case of no response, it will keep sending reminders in a loop until the due date is reached.
    
    Alternative flow:
    A1: If the user hasn’t added a due date and other information for a task in the list, it will continue asking those information (via email) at certain intervals.
```  
  2. Calculate Rewards based on Team Members’ Performance
  
 ``` 
  Precondition: With addition to the preconditions for use case 1 where user add tasks with due date and predicted no. of hours to complete it and optionally updating progress,
User must also input the completion date and no. of hours after finishing the task.

  
  Main Flow: At certain intervals[S1], the bot will evaluate each member's’ performance based on a rule-based logic system and calculate score & rewards[S2], and update the leaderboard of the team[S3] and [S4] will give new targets and set new competitions for the members
(e.g. the rule-based logic system may have a logic to give more score the faster one completes the task. Detail logic will be added later)
  
  Subflows:
  S1: It will keep track of time and will get activated after certain intervals.
  S2: It will evaluate all members’ performance based on current information available according to its logic system and calculate score & rewards.
  S3: It will update the leaderboard for the whole team.
  S4: It will set new targets for each member and set up new competition weekly.
  
  Alternative flow:
  A1: In absence of adequate information for any user, it will add penalties(minimal) for inactivity to his/her score in the leaderboard.
```
  
  3. Reminder Buddy
```
  Precondition: With addition to the preconditions for use case 1 where user add tasks with due date and predicted no. of hours to complete it and optionally updating progress, User must also input the completion date and no. of hours after finishing the task.
  
  Main Flow: The bot will ask for progress to each member based on his tasks and due dates [S1], it will wait a certain period (differing on scenario, periods will be dynamically calculated) [S2], if response is positive, it will post congratulatory message on a public channel and award score in the leaderboard[S3], if response is negative, it will post reminder message to a public channel and add penalties in his score in the leaderboard.
  
  Subflows:
  S1: The bot will ask for progress to each member based on his tasks and due dates.
  S2: It will wait a certain period (differing on scenario, periods will be dynamically calculated).
  S3: If response is positive (response of progress), it will post congratulatory message on a public channel and award score in the leaderboard.
  S4: If response is negative (either no response/response of no progress), it will post reminder message to a public channel and add penalties in his score in the leaderboard.

  Alternative flow:
A1: 1.	If information is missing about any member, it will post message to public channel that the member is inactive.
```

### Task Tracking
Tool | Description
---  | ---
[Trello Task Manager](https://trello.com/b/MXYu6ZEy/task-manager-bot) | Used for task tracking like worksheet.
[Github Issues](https://github.ncsu.edu/yhu22/CSC510_F17_Project/issues) | Issues to be solved for the implementation.
[Testing Board](https://trello.com/b/3L2DxAis/test-board) | Trello board for us to test the function.
[Demo Board](https://trello.com/b/5LYE5kJE/demo-board) | Trello board for demo.

Reference |
--- |
https://api.slack.com/incoming-webhooks |
https://github.com/thisbejim/Pyrebase |
https://pypi.python.org/pypi/python-firebase/1.2 |
https://api.slack.com/rtm |
https://github.com/slackapi/python-slackclient |
