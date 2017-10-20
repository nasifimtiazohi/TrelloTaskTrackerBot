## Bot

In this milestone, you will begin developing your bot based on your accepted design proposal.

The primary focus of this milestone will be to integrate with the bot platform for your bot and develop the interaction component of your bot.

There are also several techniques (such as testing and mocking) and practices (agile) that you will be required to perform as part of this milestone.

### Use Case Refinement (contains 10% : done)

Based on the feedback from your design milestone, improve the use cases for your bot. This should be your final iteration of your use case design, it will be very difficult to change past this point.

Describe how you address any required fixes to your use cases.

### Mocking Service Component (required - 20%)

### (required) mock.json file for trello data (person 2)
### (required) how to create mock output data-- similar json file ? (person 2)
### (required) what is injection?
Because the focus on your milestone is platform integration and bot interaction, you will not yet have a working service implementation. Implement mock services and data to support service integration. For example, if you were implementing a meeting bot that helps set up meetings, use mock calendar data to determine available meeting time, rather than integrate with a user's Google calendar.

**Failure to use appropriate mocking/injection techniques will result in 0 credit**. Do not do this:

```
bot.hears("command", function(){ bot.replys("fake answer");});
```

### Bot Implementation
### (done) deplying bot in slack project team that can respond to basic command
### (done) make trello api calls to fetch/post to project team board
### (required) make commands for 3 use cases -- what shall be a full conversation (person 1,3)
### (required) make timer for bot (person 1,3)
### (required) make the bot provide push notifications on specific time (person 1,3)
* **Bot Platform (15%) : required **

In implementing your bot, you will have to primary tasks:

* **Bot Platform (done -15%)**: Implement hooks into platform. You should be able to have a fully operational bot within your platform (Slack/Github) that can response to basic commands.
* **Bot Integration (required - 15%)**: Implement basic conversation/interaction with bot. You need to support the ability to fully have a conversation with an bot as defined by your use cases.

### Selenium Testing (required - 20% )

### (required) person 4

To support testing of your bot, we will use Selenium to verify that the bot is returning the correct response based on a input message.

[See full example Selenium test for Slack](https://gist.github.com/chrisparnin/e3ee1a96c681f12ae11246cfe3225182)

```java
@Test
public void postMessage()
{
	driver.get("https://csc510-fall16.slack.com/");

   ...

	// Find email and password fields.
	WebElement email = driver.findElement(By.id("email"));
	WebElement pw = driver.findElement(By.id("password"));

   ...
```

Create a selenium test that demonstrates each use case. Demonstrate at least one "happy path" and one "alternative" path for each use case.

### Task Tracking ( required - 15%)

### (required- person 5)

Building software is a complex process and you will have a big team of people. The only way you will make it through this process is by careful planning and delegation of work.

You will report the progress of each week (iteration). To track this, you will submit a completed iteration worksheet at the end of the iteration (include in WORKSHEET.md). This will describe the tasks completed for your use cases.

An example sheet follows:

##### Week 1

| Deliverable   | Item/Status   |  Issues/Tasks
| ------------- | ------------  |  ------------
| Use Case      | Get Meeting Availability          | &nbsp;
| Subflow      | 1             |  #33, #38, #78
| Subflow      | 2             |  [Pivotal Task](https://www.pivotaltracker.com/story/show/114636091)
| Subflow      | 3             |  [Trello Card](https://trello.com/c/diA1DaMw)
| Subflow      | &nbsp;        | &nbsp;
| Selenium Tests| Incomplete    | Get Meeting Availability, error1,...

* Github issues in a markdown referred to as `#33` will automatically turn into links when in same repo.
* You can link to trello cards by click on share inside a card to get a link.
* You can link to pivotal stories by clicking on the first button left of ID in detail view.
* You reuse the markdown of the above table for your worksheet.

#### Stories and Tasks

Advice: You should practice agile by breaking use cases down into smaller stories and tasks and plan how to test, implement, and deliver those changes each week. Because you need to deliver a use case almost every week, you might consider having tasks that separately handle different layers of system. You will find this is a common situation in an agile team. Some suggested breakdowns include:

* Design
* Reports, scrum master, planning
* Creating database tables
* Creating mocking data
* Scripting selenium
* Bot interaction
* Slack intergration
* Message conversation
* Service connections 

Finally, you may find the [SMART](https://www.mindtools.com/pages/article/smart-goals.htm) method a good way plan tasks.

Creating tasks on the last day of submission **will not receive credit**. Plan ahead.

### Screencast (required- 5%)


### (required- person 5)

Create a screencast of your bot performing your three use cases.
Demonstrate your selenium tests being executed.

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
