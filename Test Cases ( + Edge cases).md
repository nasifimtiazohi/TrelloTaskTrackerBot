
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


































































