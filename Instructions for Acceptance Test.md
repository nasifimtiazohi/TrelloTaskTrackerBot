## General Instructions:

1.	The corresponding slack profile and trello profile need to be matched. One way of matching could have been the mail address of both profile. However, there lies two problems in this way. 1) Trello tokens doesn’t return mail id of other members 2) Any slack user can change his/her mail id at any time.
So, we did a name matching between slack full name and trello full name. The names shouldn’t be exactly the same, but a reasonable match should be there. (like “sheikh Nasif Imtiaz” in trello and “Nasif Imtiaz Ohi” in slack matches).
If anyone wants to open a new profile in both slack and trello, these should be kept in mind.

2.	The Trello Board has one card for each task.  There are labels for each card which have specific meanings for our Slack bot:

***We have based all calculations based on labels in Trello to ensure the use of labels for the bot. To mark a card complete, we considered only "green label", not the default checkbox in trello. Hence, to mark a card complete and stop getting messages in Usecase 1 and 3 or get points in usecase 2, one has to label it green.***

     **Progress of Task:**

     *Red label - to do (task not finished yet)*

     *Green label - Done*

     **Difficulty of Task:**

     *Yellow - Easy*

     *Sky Blue – Medium*

     *Black- Hard*

     Red label represents a task in “ongoing”; Green label means a task is done. Usecase 3 will not take cards without red label into account and will not ask for progress for them even if the due date is set. It only works for the cards which has red labels but not green, hence ongoing! The difficulty of task is a rule we made to give different reward points to a member who completed a task. The detailed rule about calculating points and how we categorize the task in different level described in CalculateGradePrinciples.md

     However, Usecase 1 only considers due date (as it gets activated when a card approaches due date) and difficulty labels. In absence of those, it will send mails to prompt the user (if any assigned) to fill up the necessary labels.

     For cards which doesn’t have any members assigned, our bot doesn’t do anything about that, this is a responsibility for a user to set corresponding labels.

3.	All of our use cases are meant to run automatically at certain intervals for which we have implement threading. The threading delays are -
one hour for usecase 1 and 3, and one day for usecase 2

however to trigger use case 2 manually, there are also 2 commands.

## Instruction for USECASE 1:

### Main Flow
1.	This usecase gets activated per every interval (one hour)
2.	Bot will read all the cards from trello board which have due date set and difficulty labels set.
3.	If due date and difficulty labels are set it will go to the main flow (step 5)
4.	[Alternate flow] If an unfinished(not labelled green) card does not have due date and difficulty labels set, it will send the assigned user (if any) a mail to fill up the necessary labels and go to step 6. If a card even has no members assigned, the bot has nothing to do.
5.	[Main flow], if a card is easy(yellow) and has due time within 12 hours and not finished(not labelled green), it will send the user a mail.
if a card is medium(sky) and has due time within 24 hours and not finished(not labelled green), it will send the user a mail.
if a card is hard(black) and has due time within 48 hours and not finished(not labelled green), it will send the user a mail.
6.	A user has to take an action for the sent mails. For alternate flow, the user must fill up both the due time and difficulty labels. And for main flow, the use must label the card green to mark “finished”.
When the next time the bot(thread for usecase 1) gets activated, it will check for all things again. If the user has taken proper steps, it will not send any more mail. If there’s no action, the bot will keep sending mails again. {hence, nagging reminder}

### Usage instructions
To check USECASE 1, the TAs can set up different cards with different due time and difficulty labels. If the bot sends mail for a card which follows the criteria, the usecase works. Then if the user has taken proper action, the bot will stop sending mails. Otherwise new mails will come at every interval period.

## Instruction for USECASE 2:
### Main Flow
1. It will keep track of time and will get activated after certain intervals.
2. It will evaluate all members’ performance based on current information available according to its logic system and calculate score & rewards.
3. It will update the leaderboard for the whole team.
4. It will set new targets for each member and set up new competition weekly.
### Alternative Flow
1. In absence of adequate information for any user, it will add penalties(minimal) for inactivity to his/her score in the leaderboard. The leaderboard score will get update everyday

### Usage instructions
1. TAs can set up different cards with different due time and difficulty labels. ([Demo Board](https://trello.com/b/5LYE5kJE))
2. Invoke usecase2 by typing "@taskbot show leaderboard" and "@taskbot show targets board" in the slack taskbot channel. The target will get update everyweek.

## Instruction for Usecase 3
### Implementation Details
This usecase get all the cards about to due and ask for input of user and respond to user input accordingly.
* If the user completes the task, we will do the following things
     1. We will update his progress (="completed") in database and also update the points to his total points (reward)
     2. We will update trello board as well, mark the card as DONE(become green label) automatically
     3. we will send congratulation message in public channel, so user's teammate can find their motivation of working harder to beat others
* If the user ignores our reminder, or he provide an negative response,
     we will do the following things:
     1. We will update his progress (="pending")in database and also update the points to his total points (deduct his/her total points -- penality)
     2. Keep sending the reminder
### Step to step instructions
1. Open the following website: https://510taskmanagerbot.slack.com
2. Login as CSC510_TA account (described in [TA_account_info.txt](https://github.ncsu.edu/yhu22/CSC510_F17_Project/blob/master/TA_account_info.txt))
3. Go to Apps-> taskbot, if you receive message from taskbot
4. Respond **negatively**, In input box, input "@taskbot > not yet": you will receive a message as reminder in "general" channel
5. Respond **positively**, In input box, input "@taskbot > completed" : you will receive a congratulation message in "general" channel and also be informed of your points in total.

(Label of card will change according to user's input command)
