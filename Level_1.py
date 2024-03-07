import mysql.connector
import math

# Establish connection
connection = mysql.connector.connect(host='localhost',
                                     database='MyDB',
                                     user='root',
                                     password='Root123@')

# Create cursor object
cursor = connection.cursor()

# 1) Implement a python code that finds the probability of selection of 2 from Marvel and 3 from DC teams.
def calculate_probability(num_members, r):
    num_combinations = math.comb(num_members, r)
    total_possible_combinations = math.comb(num_members, r)
    probability = num_combinations / total_possible_combinations
    return probability

# Query to get number of members in Marvel and DC teams
cursor.execute("SELECT COUNT(*) FROM Marvel")
marvel_members_count = cursor.fetchone()[0]

cursor.execute("SELECT COUNT(*) FROM DC")
dc_members_count = cursor.fetchone()[0]

marvel_probability = calculate_probability(marvel_members_count, 2)
dc_probability = calculate_probability(dc_members_count, 3)

print("Probability of selecting 2 from Marvel Team:", marvel_probability)
print("Probability of selecting 3 from DC Team:", dc_probability)

# 2) List all those stars who are heavier than SpiderMan and taller than Henery.
def find_stars_heavier_and_taller(cursor, marvel_team, dc_team):
    cursor.execute("SELECT * FROM " + marvel_team)
    marvel_members = cursor.fetchall()

    cursor.execute("SELECT * FROM " + dc_team)
    dc_members = cursor.fetchall()

    spiderman_weight = None
    for member in marvel_members:
        if member[1] == 'SpiderMan':
            spiderman_weight = int(member[3])
            break

    if spiderman_weight is None:
        return "SpiderMan not found in the Marvel team"

    henery_height = None
    for member in dc_members:
        if member[1] == 'Henery':
            henery_height = int(member[2])
            break

    if henery_height is None:
        return "Henery not found in the DC team"

    stars = [member[1] for member in dc_members if float(member[2]) > henery_height and float(member[3]) > spiderman_weight]
    return stars

stars = find_stars_heavier_and_taller(cursor, "Marvel", "DC")
print("Stars heavier than SpiderMan and taller than Henery:", stars)


# 3) List all those stars who have played more than 100 games and are heavier than Captain America.
def find_stars_heavier_and_more_games(cursor, team, min_games_played):
    cursor.execute("SELECT * FROM " + team)
    team_members = cursor.fetchall()

    captain_america_weight = None
    for member in team_members:
        if member[1] == 'CaptainAmerica':
            captain_america_weight = int(member[3])
            break

    if captain_america_weight is None:
        return "Captain America not found in the team"

    stars = [member[1] for member in team_members if int(member[3]) > captain_america_weight and int(member[4]) > min_games_played]
    return stars

stars = find_stars_heavier_and_more_games(cursor, "Marvel", 100)
print("Stars with more than 100 games played and heavier than Captain America:", stars)

# 4) For the given dataset representing stars from the Marvel and DC teams, if a metaverse is to be formed where the summation of the stats (height, weight, and games played) of any star is greater than 350 units, then display the names of all the stars meeting this criterion.
def find_stars_metaverse(cursor, team1, team2, threshold):
    metaverse_stars = []

    cursor.execute("SELECT * FROM " + team1)
    team1_members = cursor.fetchall()

    cursor.execute("SELECT * FROM " + team2)
    team2_members = cursor.fetchall()

    for member in team1_members + team2_members:
        if sum(int(value) for value in member[2:]) > threshold:
            metaverse_stars.append(member[1])

    return metaverse_stars

metaverse_stars = find_stars_metaverse(cursor, "Marvel", "DC", 350)
print("Stars in the metaverse:", metaverse_stars)

# Close cursor and connection
cursor.close()
connection.close()


