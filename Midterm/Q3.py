def howDidTheCowboysDo(filename):
    cowboys_wins = 0
    last_win_year = 0
    winners_list = []


    with open(filename, 'r') as file:
        for line in file:
            winners_list.append(line.strip())

    for index, team in enumerate(winners_list, start=1967):
        if team == "Dallas Cowboys":
            cowboys_wins += 1
            last_win_year = index

    return cowboys_wins, str(last_win_year), winners_list



