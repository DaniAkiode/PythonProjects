# Dictionary containing players and the goals they have scored prior to April 2024
players = {"Cristiano Ronaldo": 754, "Lionel Messi": 731, "Erling Haaland": 236, "Kylian Mbappe": 281}

# Custom function to get the score of a player
def get_goals(player):
    return player[1]

# Sorting the players based on their scores, using the custom function as key
sorted_players = sorted(players.items(), key=get_goals, reverse=True)

# Printing the sorted players
for player, goals in sorted_players:
    print(player, goals)