# Reward Principles 
## Work flow
1. design leaderboard (where to put score, hours of work, task finish time) 
2. design database schema 
3. read data from trello, save to database 
4. write function to calculate reward points 
5. save the points to database 
6. present the point in trello
7. Configure database, implement database and bot connection

## Leaderboard score calculation Function

There are two factors we are using to reward the out-performed users: task difficulty and working efficiency.
1. Task Difficulty (Pts)

|Hours of Work | Difficulty | Reward Points 
|--- | --- |---
|> 6h | HARD |50
|3h < T < 6h | Median | 30
|< 3h | EASY|10

2. Working Efficiency BPts

|Finish Time before deadline | Bonus Reward Points
|--- | ---
|>=3h | 30
|1h< T< 3h | 15
|<= 1h| 0

Final score = Pts + Bpts
This is the score that shoud be stored in leaderboard and present to the user.

3. Deduction Points
|Time passed Deadline| Penality 
|--- | --- 
|<= 12h | -10 
|<= 24h |-30
|>24| -50 
