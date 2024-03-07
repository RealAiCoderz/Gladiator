import mysql.connector

# Function to calculate probability based on criteria
def calculate_probability(cursor, team_table, criteria):
    cursor.execute("SELECT * FROM " + team_table)
    team_data = cursor.fetchall()
    total_players = len(team_data)
    players_meeting_criteria = [player for player in team_data if criteria(player)]
    probability = len(players_meeting_criteria) / total_players
    return probability

# Function to calculate team formation probability based on criteria
def calculate_team_probability(cursor, team1_table, team2_table, criteria):
    cursor.execute("SELECT * FROM " + team1_table)
    team1_data = cursor.fetchall()
    cursor.execute("SELECT * FROM " + team2_table)
    team2_data = cursor.fetchall()
    total_combinations = 0
    valid_combinations = 0

    for player1 in team1_data:
        for player2 in team2_data:
            for player3 in team2_data:
                total_combinations += 1
                if criteria(player1, player2, player3):
                    valid_combinations += 1

    probability = valid_combinations / total_combinations
    return probability

# Function to check tournament criteria
def tournament_criteria(player):
    return int(player[2]) > 180 and int(player[4]) > 50

# Function to check team formation criteria
def team_criteria(player1, player2, player3):
    combined_weight = int(player1[3]) + int(player2[3]) + int(player3[3])
    return (int(player1[3]) < 80 or int(player2[3]) < 80 or int(player3[3]) < 80) and combined_weight <= 250

# Establish connection
connection = mysql.connector.connect(host='localhost',
                                     database='MyDB',
                                     user='root',
                                     password='Root123@')

# Create cursor object
cursor = connection.cursor()

# Calculate probability for tournament selection criteria
marvel_tournament_probability = calculate_probability(cursor, "Marvel", tournament_criteria)
dc_tournament_probability = calculate_probability(cursor, "DC", tournament_criteria)
overall_tournament_probability = marvel_tournament_probability * dc_tournament_probability
print("Probability that both selected players meet the criteria for the tournament:", round(overall_tournament_probability,3))

# Calculate probability for team formation criteria
team_probability = calculate_team_probability(cursor, "Marvel", "DC", team_criteria)
print("Probability of forming a team with given criteria:", round(team_probability,3))

# Close the connection
connection.close()
