# Task Manager BOT Final Report #

### Screencast of Task Manager BOT
[Screencast]()

### Group Members

Name | Unity ID
--- | ---
Xiaoting Fu | xfu7
Yu-Ching Hu | yhu22
Nasif Imtiaz | simtiaz
Guanxu Yu | gyu9
Vinay Gupta | vgupta8

### Problem Solved by Task Manager

In software engineering field, a project is always divided into multiple parts for each developer.
Sometimes your work might depend on others work (concurrent issue), with our task manager BOT, it
is unnecessary to keep asking the progress of your colleagues. Our BOT will notify every member in
the same channel that who completed what work. This can reduce the overhead of tracking others' progress
such as personal message or emails.
On the other hand, from the lecture, we know that the average working hours are 2 hours per day for each engineer if lucky (No other disturbing things
    such as meeting, business trip and so on). To improve the productivity of a developer, our BOT will calculate reward points for developers that
    finish the assigned tasks. It will display the leaderboard and next target board for you to achieve. The BOT will post congratulation message as well as reminder message
    in public channel to alert everyone that whose contribution is not enough and need to work hard.
    This can be viewed as peer pressure that urge you to code more and make more contribution.
Besides, we all need some tools to help us tracking many tasks. Our BOT also has a function that will send the user a reminder email for pending task and it just like an annoying alarm clock did not go off if you don't complete your task.

### Primary Features
Nowadays, since collaboration between programmers become more and more common. Online development platform like Github, group discussion forum like Slack and Task Management tool like Trello emerged. However, none of these tools can promote group work in a simple manner. Therefore, the lack of task mangement tool for software developer and also engineers motivate our project. We design a task management bot that reside in Slack group forum (running as a server deamon) detecting new changes from Trello team board and send message or request message accordingly.

There are four significant features of our bot:
1. Integrate Trello and Slack
As we know Slack and Trello are two different platform, by integrating these two platform, our bot is able to fetch and update data from Trello and post a summary of the information in Slack.
2. User-friendly
We are able to handle unexpected commands, for example if user input "@taskbot done > " without a task name, our bot will respond with handle
3. 
### Reflection on Development Process and Project

### Limitations and Future Work
