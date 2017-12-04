# Task Manager BOT Final Report #

### Screencast of Task Manager BOT
[Screencast](https://drive.google.com/a/ncsu.edu/file/d/1DSNOAnb9GNwX-kY-Ejr5I1xG2Oc6z8lm/view?usp=sharing)

### Group Members

Name | Unity ID
--- | ---
Xiaoting Fu | xfu7
Yu-Ching Hu | yhu22
Nasif Imtiaz | simtiaz
Guanxu Yu | gyu9
Vinay Gupta | vgupta8

### Problem Solved by Task Manager

### Primary Features

### Reflection on Development Process and Project

The above sections are described in detail in [CSC510 Final Report](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/master/CSC510%20Final%20Report.pdf)

#### Design 

We have two phases for this stage. One is project design, which means we need to decide what we want for this bot, what functions and services should our bot have. The other one  is how we design our basic software architecture. For project design, we have some meetings to talk about it. And I think we really did a good job at this part. We start from a basic idea -- task manager, then we extend its functions by exploring current functions in Trello. Next, we analize what we can do better by collaborate Trello and Slack. And finally we dicided to enable those primary features above. For the second part, software architecture, we designed basic components of our bot and how they interact with each other. In sum, I think we really did a good at this phase.

#### Bot 

At this stage, we implement basic components and setup infarstructures for our bot. But here, at real implementation, I think there still more things to do. First, I think we do not clearly decouple modules from every usecase. In other words, different usecases may reimplement lots of code. In fact, they could share some common modules to avoid duplicated code. Second, I think we didn't design good interfaces and templates for these 3 usecases. The consequence is that it is hard for the developer of one usecase to make contribution for other usecases. I think in the futher, when we start to implement a new project, it is important to take some time to think about how to keep the code simple and easy to comprehend.

For the mocking and testing part, we are using fake Trello card created by ourselfs and then implement selenium testing.

For the Task Tracking part, we used Trello to track our progress. We set up list for every week and we setup cards for every teammember. Tracking progress is good for imporving the performance of the whole team. And it is a easy way to evaluate the performance of every teammember.

#### Service

In this milestone, we prolished our code, and implemented main flows of our service. And then we incorporated everyone's code. Here we meet lots of issues like conflicts between each usecase, concurrency issue, etc. Those issues caused a lot of trouble and affects our efficiency a lot. After that, we need to think the reasons of those problems and consider how to avoid that situation next time. We did not have a design review before the implementation of our service. So everyone had own understand about how the bot looks like and how to implement the bot. Thus, this will affect the usage of our resources. That's where the conflicts come from. The solution will be use a lock to protect shared resources and reduce race condition. Then we could maintain concurnency for multi-threading. Another main issue is the namespace issue. At first, we just simply collect everyone's code and put it in one file. But we got lots of name conflicts and running time errors. To solve that, we make everyone's code as a module and call the a  usecase service from the corresponding module. And also, we should think about using design patterns to help us organizaing code. 
