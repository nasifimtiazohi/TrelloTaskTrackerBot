# Task Manager BOT #

### Link to Screencast for BOT Milestone
Screencast:


### Group Members

Name | Unity ID 
--- | --- 
Xiaoting Fu | xfu7
Vinay Gupta | vgupta8
Nasif Imtiaz | simtiaz
Yu-Ching Hu | yhu22
Guanxu Yu | gyu9

## Milestone - BOT ##

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
  

