# Reward Principles 
## Leaderboard score calculation Function

There are two factors we are using to reward the out-performed users: task difficulty and working efficiency.
1. Task Difficulty (Pts)

|Hours of Work | Difficulty | Reward Points 
|--- | --- |---
|> 6h | HARD |50
|3h < T < 6h | Median |
|< 3h | EASY|10

2. Working Efficiency BPts

|Finish Time before deadline | Bonus Reward Points
|--- | ---
|>=3h | 30
|1h< T< 3h | 15
|<= 1h| 0

Final score = Pts + Bpts
This is the score that shoud be stored in leaderboard and present to the user.
