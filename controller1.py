
import math

class TeamController:
  
    def probability_of_selection(team1, team2, num_from_team1, num_from_team2):
        total_players_team1 = len(team1.members)
        total_players_team2 = len(team2.members)

        probability_team1 = (num_from_team1 / total_players_team1) * ((num_from_team1 - 1) / (total_players_team1 - 1))
        probability_team2 = (num_from_team2 / total_players_team2) * ((num_from_team2 - 1) / (total_players_team2 - 1))

        return probability_team1 * probability_team2

   
    def find_heavier_taller_players(team1, team2, spiderman_weight, henery_height):
        result = []
        for member in team1.members + team2.members:
            if member.weight > spiderman_weight and member.height > henery_height:
                result.append(member.name)
        return result

 
    def find_players_more_than_games_and_heavier_than(team1, team2, games_threshold, captainamerica_weight):
        result = []
        for member in team1.members + team2.members:
            if member.games_played > games_threshold and member.weight > captainamerica_weight:
                result.append(member.name)
        return result

    
    def find_metaverse_stars(team1, team2):
        result = []
        for member in team1.members + team2.members:
            if member.height + member.weight + member.games_played > 350:
                result.append(member.name)
        return result

    
    def calculate_mean(values):
        return sum(values) / len(values)

    
    def calculate_median(values):
        sorted_values = sorted(values)
        n = len(sorted_values)
        if n % 2 == 0:
            mid1 = sorted_values[n // 2 - 1]
            mid2 = sorted_values[n // 2]
            return (mid1 + mid2) / 2
        else:
            return sorted_values[n // 2]

    
    def calculate_deviation(values, mean):
        return [value - mean for value in values]

  
    def calculate_standard_deviation(values, mean):
        squared_deviations = [(value - mean) ** 2 for value in values]
        variance = sum(squared_deviations) / len(values)
        return math.sqrt(variance)

    def get_valid_input(message, lower_limit, upper_limit):
        while True:
            try:
                value = float(input(message))
                if lower_limit <= value <= upper_limit:
                    return value
                else:
                    print(f"Input must be between {lower_limit} and {upper_limit}. Try again.")
            except ValueError:
                print("Invalid input. Please enter a numeric value.")