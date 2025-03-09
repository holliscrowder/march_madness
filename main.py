# Take two team names and determine the winner
import random

team1 = "Golden State Warriors"
team2 = "Denver Nuggets"

def determineWinner(team1, team2):
    odds = random.randint(0,1)
    if odds > 0.5:
        winner = team2
    else:
        winner = team1

    return winner

print(determineWinner(team1, team2))