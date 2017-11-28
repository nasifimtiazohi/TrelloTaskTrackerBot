
| #  | Use Case | Input  | Output | Expected Output  | Result |
| ------------- | ------------- | ------------- | ------------- | ------------- | ------------- |
| 1 | 1 |No new input | Send email notifications on existing data  |Send email notifications on existing data | Pass  |
| 2 | 1 |New card - To do, Hard, within 36 hours | Send email notifications on existing data plus the new card |Send email notifications on existing data plus the new card | Pass  |
| 3 | 1 |New card - To do, Hard, Last year date | Send email notifications on existing data and not the new card |Send email notifications on existing data and not the new card| Pass  |
| 4 | 1 |New card - To do, Last year  | Send email notifications to input information for this card  |Send email notifications  to input information for this card | Pass  |
| 5 | 1 |New card - To do, Easy  | Send email notifications to input information for this card  |Send email notifications  to input information for this card | Pass  |
| 6 | 1 |New card - To do, Hard, Easy, Medium, Last year  | Send email notifications based on label medium  for this card |Send email notifications  based on label medium for this card | Pass  |


































































