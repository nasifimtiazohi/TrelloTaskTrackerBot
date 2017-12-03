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
We are able to handle unexpected commands, for example if user input "@taskbot done > " without a task name, our bot will prompt user to give a proper command
There are several cases of error we can handle.
1) User given the command that are not listed in our command set, we will prompt user to input again


2)
3. 
4.
### Reflection on Development Process and Project

#### Design 

We have two phases for this stage. One is project design, which means we need to decide what we want for this bot, what functions and services should our bot have. The other one  is how we design our basic software architecture. For project design, we have some meetings to talk about it. And I think we really did a good job at this part. We start from a basic idea -- task manager, then we extend its functions by exploring current functions in Trello. Next, we analize what we can do better by collaborate Trello and Slack. And finally we dicided to enable those primary features above. For the second part, software architecture, we designed basic components of our bot and how they interact with each other. In sum, I think we really did a good at this phase.

#### Bot 

At this stage, we implement basic components and setup infarstructures for our bot. But here, at real implementation, I think there still more things to do. First, I think we do not clearly decouple modules from every usecase. In other words, different usecases may reimplement lots of code. In fact, they could share some common modules to avoid duplicated code. Second, I think we didn't design good interfaces and templates for these 3 usecases. The consequence is that it is hard for the developer of one usecase to make contribution for other usecases. I think in the futher, when we start to implement a new project, it is important to take some time to think about how to keep the code simple and easy to comprehend.

For the mocking and testing part, we are using fake Trello card created by ourselfs and then implement selenium testing.

For the Task Tracking part, we used Trello to track our progress. We set up list for every week and we setup cards for every teammember. Tracking progress is good for imporving the performance of the whole team. And it is a easy way to evaluate the performance of every teammember.

#### Service

In this milestone, we prolished our code, and implemented main flows of our service. And then we incorporated everyone's code. Here we meet lots of issues like conflicts between each usecase, concurrency issue, etc. Those issues caused a lot of trouble and affects our efficiency a lot. After that, we need to think the reasons of those problems and consider how to avoid that situation next time. We did not have a design review before the implementation of our service. So everyone had own understand about how the bot looks like and how to implement the bot. Thus, this will affect the usage of our resources. That's where the conflicts come from. The solution will be use a lock to protect shared resources and reduce race condition. Then we could maintain concurnency for multi-threading. Another main issue is the namespace issue. At first, we just simply collect everyone's code and put it in one file. But we got lots of name conflicts and running time errors. To solve that, we make everyone's code as a module and call the a  usecase service from the corresponding module. And also, we should think about using design patterns to help us organizaing code. 

#### Deploy

### Limitations and Future Work
