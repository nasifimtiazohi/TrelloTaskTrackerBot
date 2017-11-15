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

| Difficulty | Reward Points 
| --- |---
| HARD |50
| Median | 30
| EASY|10

2. Difficulty color

|Difficulty | color
|---|---
|Easy |yellor
|Median |sky
|Hard |black

Final score = Pts + Bpts
This is the score that shoud be stored in leaderboard and present to the user.

3. Deduction Points

|Difficulty| Penality 
|--- | --- 
| Hard | -10 
| Median | -30
| Easy | -50 
