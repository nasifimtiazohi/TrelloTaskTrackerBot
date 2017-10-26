# Task Manager BOT #

### Link to Screencast for BOT Milestone
[Screencast](screencast_file_path_put_here)

### Files Related to BOT Milestone

File | Description
---  | ---
usecase1n3/firsttest.py | Main file. Run this to activate BOT in Slack
usecase1n3/slackapicall.py | Make Slack API calls
usecase1n3/trellocall.py | Make Trello calls and run functions for usecase 1 & 2
usecase1n3/usecase3.py | Run functions for usecase 3
usecase1n3/emailing.py | Code for sending mail
usecase1n3/mock.json | Mock data 
Selenium Test/BotTest.java | Selenium test for BOT
Selenium Test/SeleniumTestForSlack.java | Selenium test for Slack

### Group Members

Name | Unity ID 
--- | --- 
Xiaoting Fu | xfu7
Vinay Gupta | vgupta8
Nasif Imtiaz | simtiaz
Yu-Ching Hu | yhu22
Guanxu Yu | gyu9

## Milestone - BOT ##
Our bot runs on the assumption that a team will have their workspace both on "Slack" and "Trello". They use trello to keep track of their tasks, and "Slack" for communication. With necessary permissions, our bot resides in Slack and also can fetch/post data on Trello workspace of the team. 

For testing purpose for TAs,
https://join.slack.com/t/510taskmanagerbot/shared_invite/enQtMjU0Njk4NDA4NzExLTM2ZmMyNzEwNTA3ZjgyNmQwZDk1Y2VlMjU4NWQ3ZDlmYWYwODhiMDYwOGU2ZmRhZmMxOGQ1ZTYxZWI3ZDllNDQ -
is the link for invitation to our team's slack workspace where our bot resides. Also, we can send invitaion to our trello team if the TAs want. 


### Use Cases ###    

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

### Mocking Service Component

The main data source for our bot will be trello boards and its cards. Also it would require some information from Slack. And for other necessary information, it will ask users on the slack and capture and store their response.

For this milestone, we have filled our trello team's board with mock data to work with. We can make trello api calls to fetch this data and can also make slack api calls to get necessary information.

However we will require users' input in future which we will store in our database. We don't have that data yet. Also, some information are yet not available to get through api calls. For those data, we wrote a **mock.json** file to hardcode those information in json format. Whenever we needed those types of data for any service/testing, we just read that file as our data source. That is how we implemented mocking.

### Bot Implementation

* **Bot Platform : **

* **Bot Platform**: We have successfully deployed our bot into the slack workspace. It can also make the necessary api calls to trello workspace. It can respond to/send basic commands based on the usecases. 
If you run the firsttest.py file the bot will get active in the workspaces. [ you will need to install necessary libraries. you can create a virtualenv and pip install "slackclient" and "trello" ]

* **Bot Integration (required - 15%)**: 
1. It can understand command for 3 use cases; the format is harcoded. [format will be explored more in future]. 
2. It can send message in any channel 
3. It can recieve message in any channel and can understand/respond to it if they are under certain formats. 
4. It can direct message to any user and capture response. 
5. It can send mail to the users. 

### Selenium Testing 
## Overview
We conducted Selenium testing based on Chrome, and fixed the JUnit testing orders.
The four JUnit tests we haved conducted are 
 * "sendNaggingReminder"
 * "testEmailSent"
 * "performanceEvaluation"
 * "reminderBuddy"
 
 ## Usecase 1: Send Nagging Reminder
 * Test the following functionalities:
	 * Input "@firsttest usecase 1" command to slackbot
	 * Firsttest bot respond by sending the names of users who has task that is due within 1 day deadline
	 * Sends a Email to his/her email address
 * The test cases for this usecase are "sendNaggingReminder and "testEmailSent.
 	 * sendNaggingReminder
   *    Check if the bot respond the names of three persons who have task unfinished (based on our mock data)
   * testEmailSent
   *    Check if the email is sent to these person by checking the sender's gmail box with the timestamp same as the person input the command to the bot
 
 
## Usecase 2: Performance Evaluation
 * Test the following functionalities:
	 * Input "@firsttest usecase 2" command to slackbot
	 * Firsttest bot respond by sending the names of users as long as their performance score
 * The test case related to this usecase is "performanceEvaluation"
 	 * performanceEvaluation
   *    Check if the five users along with their score are printed by the bot
 
 
 ## Usecase 3: Reminder Buddy
 * Test the following functionalities:
	 * Input "@firsttest usecase 3" command to slackbot
	 * Firsttest bot respond by sending direct message to the person who has task unfinished
 * The test case related to this usecase is "reminderBuddy"
 	 * reminderBuddy
   *    check if the last sentence of the chat screen is "what is your progress, mate?"

### Task Tracking
[WORKSHEET](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/master/WORKSHEET.md)

### Reference
https://api.slack.com/incoming-webhooks

This link contains 
1. send timely messaged 
2. message in a rich format [ although not by our bot. by the integrated incoming-webhook-bot of slack]

https://api.slack.com/rtm
The one that we are using

**You cannot provide attachments nor buttons to messages posted over the RTM API.
If your bot user needs to send more complex messages, use the web API's chat.postMessage or chat.postEphemeral.**
