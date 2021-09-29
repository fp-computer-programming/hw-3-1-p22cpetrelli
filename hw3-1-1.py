#author CJP 9/29/2021

team1_wins = input("How many wins does team one have? ")
team1_ties = input("How many ties does team one have? ")
team2_wins = input("How many wins does team one have? ")
team2_ties = input("How many ties does team one have? ")

team1_points = (int(team1_wins) * 3) + (int(team1_ties))
team2_points = (int(team2_wins) * 3) + (int(team2_ties))
if team1_points < team2_points:
    print(" Team 2 wins")
else:
    print("team 1 wins")