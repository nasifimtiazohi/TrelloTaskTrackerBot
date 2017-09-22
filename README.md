# Task Manager BOT #

## Milestone 1 ##
### Problem Statement ###
Efficient task management for a team, or even for a person, is one of the major challenges in software engineering. There are many platforms (e.g. trello, github) which help in this cause by allowing users to maintain lists of their “To do” tasks alongside with necessary information. But sometimes an engaging interaction may be helpful for the user to really help him/her follow up their work. For example, a person may write down his “To do” list but in real can have no impetus to further checking it in due time. But if there were an entity like a real life person who would constantly and efficiently track the progress and notify the user working as a smart reminder, more can be gained.

Also from a team point of view, often an independent entity is required to continuously evaluate each member’s performance and intelligently assign new tasks to the suitable person based on his/her skill set and previous workload. Many artificial solutions are already there, but making them as interactive and engaging as possible still remains a problem in the domain.

### Bot Description ###
Although efficiently performing these jobs can directly contribute to the eventual performance gain, the uninteresting nature of them makes it difficult to attract people to perform them. Moreover, the repetitive and rule-based logic of such tasks makes it possible for automation, thus saving a lot of resources in the process. Thus a bot could be the best solution to address jobs mentioned in the problem statement having a constant presence in those task managing platforms just like a real-life person.

Our bot does not have a conversation in the typical meaning with the user, but it would ask the users for different inputs from time to time, store them in its memory,  and send reminders/suggestions/motivations in a message-like manner. The best fit for the bot could be the “Space Responder” category.
### Use Cases ###    

  1. Smart Reminder
  2. Team Members' Performance Evaluation
  3. Intelligent Tasks Assignment

### Design Sketches ###
  *Wireframe*
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/wireframe/use_case1.jpg)
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/wireframe/use_case2.jpg)
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/wireframe/use_case3.jpg)
  
  *Storyboard*
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/storyboard/storyboard1.png)
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/storyboard/storyboard2.png)
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/storyboard/storyboard3.png)
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/storyboard/storyboard4.png)
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/storyboard/storyboard5.png)
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/storyboard/storyboard6.png)
### Architecture Design ###
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/architecture/architecture1.png)
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/architecture/architecture2.png)
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/architecture/architecture3.png)
  
  ![alt text](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/otto/architecture/architecture4.png)
### Additional Patterns ###

*Design patterns*

Singleton pattern: We use this pattern to create a client.  There are two types of clients in our application. One is used to call Trello APIs, and the other is used to connect to our central database. To lower the memory usage, we only create one client for each of these two types. 

*Builder pattern*

For each client, we use builder patterns to build a request. So we can easily to customize every request. Then the client can send the request.

