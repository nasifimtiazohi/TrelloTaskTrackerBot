## Bot

Our bot runs on the assumption that a team will have their workspace both on "Slack" and "Trello". They use trello to keep track of their tasks, and "Slack" for communication. With necessary permissions, our bot resides in Slack and also can fetch/post data on Trello workspace of the team. 

For testing purpose for TAs, << >> is the link for invitation to our team's slack workspace where our bot resides. Also, we can send invitaion to our trello team if the TAs want. 

### Use Case Refinement 

Based on the feedback from design milestone, refined use cases are presented.

### Mocking Service Component

The main data source for our bot will be trello boards and its cards. Also it would require some information from Slack. And for other necessary information, it will ask users on the slack and capture and store their response.

For this milestone, we have filled our trello team's board with mock data to work with. 

Also, we wrote a mock.json file hardcoding data that are not possible at this point to retrieve through api calls or asking the user and capturing responses. For this milestones, we used that mock data whereever we needed it to.

### (required) what is injection?

**need to polish the mocking a bit more

### Bot Implementation

* **Bot Platform : **

* **Bot Platform**: We have successfully deployed our bot into the slack workspace. It can also make the necessary api calls to trello workspace. It can respond to/ send commands.
* **Bot Integration (required - 15%)**: 1) It can understand command for 3 use cases; the format is harcoded. [format will be explored more in future]. 2) It can send message in any channel 3) It can recieve message in any channel and can understand/respond to it if they are under certain formats. 4) It can direct message to any user and capture response. 5) It can send mail to the users. 

### Selenium Testing 

### Task Tracking 


### Screencast (required- 5%)



## Deliverables

Add your code, and BOT.md document describing the following materials. [Submit here](https://docs.google.com/forms/d/e/1FAIpQLSfr5TMD-1IQFG-GYBsFrFPKrN9kl2sNfjOhVP5Hliz_G5GH8w/viewform?usp=sf_link).

* 3 Use Cases (10%)
* Mocking (20%)
* Bot Implementation (30%)
* Selenium testing of each use case (20%)
* Task Tracking -- WORKSHEET.md (15%)
* Screencast (5%)

**Other considerations**: Each team member must make contributions on a milestone (e.g., committing code, being assigned and completing tasks). Failure to perform any work will result in no credit for a team member.

DUE: Wednesday, October 25, Midnight.
