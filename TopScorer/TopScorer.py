# Dictionary containing players and the goals they have scored prior to April 2024
players = {"Cristiano Ronaldo": 754, "Lionel Messi": 731, "Erling Haaland": 236, "Kylian Mbappe": 281}

def get_goals(player):
    return player[1]

sorted_players = sorted(players.items(), key=get_goals, reverse=True)

for player, goals in sorted_players:
    print(player, goals)