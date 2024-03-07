import mysql.connector

def calculate_statistics(cursor, team_table):
    cursor.execute("SELECT Height, Weight, Games_Played FROM " + team_table)
    team_data = cursor.fetchall()

    heights = [int(row[0]) for row in team_data]
    weights = [int(row[1]) for row in team_data]
    games_played = [int(row[2]) for row in team_data]

    mean_height = sum(heights) / len(heights)
    mean_weight = sum(weights) / len(weights)
    mean_games_played = sum(games_played) / len(games_played)

    sorted_heights = sorted(heights)
    sorted_weights = sorted(weights)
    sorted_games_played = sorted(games_played)

    median_height = sorted_heights[len(sorted_heights) // 2]
    median_weight = sorted_weights[len(sorted_weights) // 2]
    median_games_played = sorted_games_played[len(sorted_games_played) // 2]

    variance_height = sum((x - mean_height) ** 2 for x in heights) / len(heights)
    variance_weight = sum((x - mean_weight) ** 2 for x in weights) / len(weights)

    std_height = variance_height ** 0.5
    std_weight = variance_weight ** 0.5

    return round(mean_height, 3), round(mean_weight, 3), round(mean_games_played, 3), \
           round(median_height, 3), round(median_weight, 3), round(median_games_played, 3), \
           round(std_height, 3), round(std_weight, 3), round(variance_height, 3), round(variance_weight, 3)

# Connecting to database
mydb= mysql.connector.connect(host='localhost',
                             database='MyDB',
                             user='root',
                             password='Root123@')

cursor = mydb.cursor()

# Calculate statistics for both teams
statistics_marvel = calculate_statistics(cursor, "Marvel")
statistics_dc = calculate_statistics(cursor, "DC")

# Print statistics for Marvel team
print("Statistics for Marvel team:")
print("Mean Height:", statistics_marvel[0])
print("Mean Weight:", statistics_marvel[1])
print("Mean Games Played:", statistics_marvel[2])
print("Median Height:", statistics_marvel[3])
print("Median Weight:", statistics_marvel[4])
print("Median Games Played:", statistics_marvel[5])
print("Standard Deviation Height:", statistics_marvel[6])
print("Standard Deviation Weight:", statistics_marvel[7])
print("Variance Height:", statistics_marvel[8])
print("Variance Weight:", statistics_marvel[9])

# Print statistics for DC team
print("\nStatistics for DC team:")
print("Mean Height:", statistics_dc[0])
print("Mean Weight:", statistics_dc[1])
print("Mean Games Played:", statistics_dc[2])
print("Median Height:", statistics_dc[3])
print("Median Weight:", statistics_dc[4])
print("Median Games Played:", statistics_dc[5])
print("Standard Deviation Height:", statistics_dc[6])
print("Standard Deviation Weight:", statistics_dc[7])
print("Variance Height:", statistics_dc[8])
print("Variance Weight:", statistics_dc[9])
