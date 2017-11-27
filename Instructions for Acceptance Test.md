## General Instructions:

1.	The corresponding slack profile and trello profile need to be matched. One way of matching could have been the mail address of both profile. However, there lies two problems in this way. 1) Trello tokens doesn’t return mail id of other members 2) Any slack user can change his/her mail id at any time.
So, we did a name matching between slack full name and trello full name. The names shouldn’t be exactly the same, but a reasonable match should be there. (like “sheikh Nasif Imtiaz” in trello and “Nasif Imtiaz Ohi” in slack matches).
If any one wants to open a new profile in both slack and trello, these should be kept in mind.

2.	The Trello Board has one card for each task.  There are labels for each card which have specific meanings for our Slack bot:

Red label - to do (task not finished yet)

Green label - Done

Difficulty of Task:

Yellow - Easy

Sky Blue – Medium

Black- Hard

Red label is used to keep track if a task in “ongoing”. Usecase 3 will not take cards with no red labels into account and won’t ask for progress for them even if the due date is set. It only works for the cards which has red labels but not green, hence ongoing! The difficulty of task is a rule we made to reward different points to a member who completed a task. The detailed rule about calculating points is in CalculateGradePrinciples.md 

However, Usecase 1 only considers due date (as it gets activated when a card approaches due date) and difficulty labels. In absence of those, it will send mails to prompt the user (if any assigned) to fill up the necessary labels.

For cards which doesn’t have any members assigned, our bot doesn’t do anything about that.

3.	All of our usecases are meant to run automatically at certain intervals for which we have implement threading. The threading delays are -
****put threading delay*****
however to trigger use case 2 manually, there are also 2 commands.

## Instruction for USECASE 1:

Flow-
1.	The usecase gets activated per every interval (put interval period)
2.	Bot will read all the cards from trello board which have due date set and difficulty labels set.
3.	If due date and difficulty labels are set it will go to the main flow (step 5)
4.	[Alternate flow] If due date and difficulty labels are set, it will send the assigned user (if any) a mail to fill up the necessary labels and go to step 6. If a card even has no members assigned, the bot has nothing to do.
5.	[Main flow], if a card is easy(yellow) and has due time within 12 hours, it will send the user a mail.
if a card is medium(sky) and has due time within 24 hours, it will send the user a mail.
if a card is hard(black) and has due time within 48 hours, it will send the user a mail.
6.	A user has to take an action for the sent mails. For alternate flow, the user must fill up both the due time and difficulty labels. And for main flow, the use must label the card green to mark “finished”.
When the next time the bot(thread for usecase 1) gets activated, it will check for all things again. If the user has taken proper steps, it will not send any more mail. If there’s no action, the bot will keep sending mails again. {hence, nagging reminder}

To check USECASE 1, the TAs can set up different cards with different due time and difficulty labels. If the bot sends mail for a card which follows the criteria, the usecase works. Then if the user has taken proper action, the bot will stop sending mails. Otherwise new mails will come at every interval period.
