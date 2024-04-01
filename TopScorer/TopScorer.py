# Dictionary containing players and the goals they have scored prior to April 2024
players = {"Cristiano Ronaldo": 754, "Lionel Messi": 731, "Erling Haaland": 236, "Kylian Mbappe": 281}

# Convert dictionary to a list of tuples
players_list = list(players.items())

#[('Cristiano Ronaldo', 754), ('Lionel Messi', 731), ('Erling Haaland', 236), ('Kylian Mbappe', 281)]

# Selection sort algorithm
for i in range(len(players_list)):
    min_idx = i  # 0 1 2 3 
    for j in range(i+1, len(players_list)):
        if players_list[j][1] > players_list[min_idx][1]:
            min_idx = j

    # Swap the minimum element with the current element
    players_list[i], players_list[min_idx] = players_list[min_idx], players_list[i]

# Print the sorted list
for player, goals in players_list:
    print(player, goals)
    
    