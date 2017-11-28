
Compilation - ~~Failed~~ Passed

~~Error in line 126 - Funtion handle_command_for_usecase3~~

| #  | Use Case | Input  | Output | Expected Output  | Result |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1 | 1 |No new input | Send email notifications on existing data  |Send email notifications on existing data | Pass  |
| 2 | 1 |New card - To do, Hard, within 36 hours | Send email notifications on existing data plus the new card |Send email notifications on existing data plus the new card | Pass  |
| 3 | 1 |New card - To do, Hard, Last year date | Send email notifications on existing data and not the new card |Send email notifications on existing data and not the new card| Pass  |
| 4 | 1 |New card - To do, Last year  | Send email notifications to input information for this card  |Send email notifications  to input information for this card | Pass  |
| 5 | 1 |New card - To do, Easy  | Send email notifications to input information for this card  |Send email notifications  to input information for this card | Pass  |
| 6 | 1 |New card - To do, Hard, Easy, Medium, Last year  | Send email notifications based on label medium  for this card |Send email notifications  based on label medium for this card | Pass  |
| 7 | 1 |New card - To do, Easy  | Send email notifications to input information for this card  |Send email notifications  to input information for this card | Pass  |
| 8 | 1 |Change thread time to 60 * 1  | Send email notifications every 60 * 1 time unit  |Send email notifications  every 60 * 1 time unit | Pass  |
| 9 | 3 |No input  | Send slack notification reminding the number of pending tasks and ask for status  |Send slack notification reminding the number of pending tasks and ask for status | Pass  |
| 10 | 3 |No input  | Database, Trello, Slack connected  |Database, Trello, Slack connected | Pass  |
| 11 | 3 |@taskbot done > tast1  | Update Database  |Update Database | Pass  |
| 12 | 3 |@taskbot done > tast1  | Update Trello label |Update Trello label | Pass  |
| 13 | 3 |@taskbot done > tast1  | Send congratulations message plus scores earned on general window in slack |Send congratulations message plus scores earned on general window in slack | Pass  |
| 14 | 3 |@taskbot done  | Handle the exception of invalid input |Handle the exception of invalid input | Pass  |
| 15 | 3 |@taskbot >  | Handle the exception of invalid input |Handle the exception of invalid input | Pass  |
| 16 | 3 |@taskbot task1  | Handle the exception of invalid input |Handle the exception of invalid input | Pass  |
| 17 | 3 |@taskbot done > invalid-input | Handle the exception of invalid input |~~Does not handle the exception of invalid input and waits for next thread execution~~ Handle the exception of invalid input| ~~Fail~~ Pass  |
| 18 | 3 |@taskbot done > already_completed_card_and_in_public_channel | Handle the exception of invalid input |~~Does not handle the exception of invalid input and gives runtime error and crashes~~ Handle the exception of invalid input| ~~Fail~~ Pass  |
| 19 | 3 | Try case sensitive inputs {@taskbot done > tast1}  | Perform all tasks  |Perform all tasks | Pass  |
| 20 | 2 | show leaderboard| Displays leader board | Displays leader board  | Pass |
| 21 | 2 | show targets board| Displays targets board | Displays targets board  | Pass |
| 22 | 2 | Invalid input command| Handles exception | Handles exception  | Pass |






































































