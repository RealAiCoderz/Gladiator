import itertools
import numpy as np
from sklearn.linear_model import LinearRegression
from controller import SupesController

def meets_selection_criteria(member):
    return member.height > 180 and member.games_played > 50

def meets_team_criteria(player1, player2, player3):
    return (player1.weight < 80 or player2.weight < 80 or player3.weight < 80) and (player1.weight + player2.weight + player3.weight <= 250)

def calculate_performance(member):
        return (member.height + member.weight)/member.games_played

def player_score(player):
        return player.height+player.weight+player.games_played

if __name__ == "__main__":
    controller = SupesController()
    marvel = controller.marvel
    dc= controller.dc
    all_members = controller.all_members
    heights= controller.heights
    weights=controller.weights

    #Question 1.1
    combinations_marvel = itertools.combinations(range(len(marvel.members)), 2)
    combinations_dc = itertools.combinations(range(dc.members), 3)
    total_combinations = 0
    valid_combinations = 0
    for combo_marvel in combinations_marvel:
        for combo_dc in combinations_dc:
            total_combinations += 1
            if len(combo_marvel) == 2 and len(combo_dc) == 3:
                valid_combinations += 1
    print("Probability of selection of 2 from Marvel and 3 from DC teams :", valid_combinations / total_combinations)


    #Question 1.2
    metaverse = []
    for i in all_members:
        if i.weight + i.height + i.games_played > 350:
            metaverse.append(i.name)
        if i.name == "SpiderMan":
            spiderman_weight = i.weight
        elif i.name == "Captain America":
            captain_america_weight = i.weight
        elif i.name == "Henery":
            henery_height = i.height

    print("Stars who are heavier than Spiderman and taller than Henery are: ")
    for i in all_members:
        if i.weight > spiderman_weight and i.height > henery_height:
            print(i.name, "\n")
    
    #Question 1.3
    print("Stars who have played more than 100 games and are heavier than Captain America are: ")
    for i in all_members:
        if i.weight > captain_america_weight and i.games_played > 100:
            print(i.name, "\n")

    #Question 1.4
    print("Stars eligible for Metaverse are: ")
    for i in metaverse:
        print(i, "\n")

    #Question 2
    print("Mean of heights: ", np.mean(heights))
    print("\nMedian of heights: ", np.median(heights))
    print("\nMean of weights: ", np.mean(weights))
    print("\nMedian of weights: ", np.median(weights))
    print("\nMean of games played: ", np.mean(controller.games_played_list))
    print("\nMedian of games played: ", np.median(controller.games_played_list))

    deviation_height = sum(abs(x - np.mean(heights) for x in heights) / len(heights))
    deviation_weight = sum(abs(x - np.mean(weights) for x in weights) / len(weights))

    print("\nDeviation of height: ", deviation_height)
    print("\nStandard deviation of height: ", np.std(heights))
    print("\nDeviation of weight: ", deviation_weight)
    print("\nStandard deviation of weight: ", np.std(weights))

    X = np.array(weights).reshape(-1, 1)
    y = np.array(controller.games_played_list)
    model = LinearRegression().fit(X, y)
    slope = model.coef_[0]
    intercept = model.intercept_
    print("\nSlope: " + slope + "\nIntercept: " + intercept)

    #Question 3

    # Filtering Marvel team members
    marvel_selected = [member for member in marvel.members if meets_selection_criteria(member)]

    # Filtering DC team members
    dc_selected = [member for member in dc.members if meets_selection_criteria(member)]

    # Calculating probabilities
    total_marvel_members = len(marvel.members)
    total_dc_members = len(dc.members)

    probability_marvel = len(marvel_selected) / total_marvel_members
    probability_dc = len(dc_selected) / total_dc_members

    # Probability that both selected players meet the criteria
    probability_both_teams = probability_marvel * probability_dc

    print("Probability that both selected players meet the selection criteria:", probability_both_teams)

    

    # Generate all possible combinations
    all_combinations = list(itertools.combinations(dc.members, 2))

    # Calculate the probability
    total_teams = len(all_combinations) * len(marvel.members)
    valid_teams = 0

    for marvel_player in marvel.members:
        for dc_players in all_combinations:
            if meets_team_criteria(marvel_player, dc_players[0], dc_players[1]):
                valid_teams += 1

    probability = valid_teams / total_teams

    print("Probability of forming a team meeting the criteria:", probability)

    #Question 4a
    #Iam assuming the taller and heaviest player who played more games has the best performance
    
    performance = {player['name']: calculate_performance(player) for player in all_members}
    best_player = max(performance,key=performance.get)

    """Limitations for this metric is that Iam not considering other factors like
    1.Expertise
    2.Awareness of game
    3.Skills, etc.
    """

    #Question 4b
    """Iam assuming the sum of all the attributes of a player to be their overall performance based on that score
    I will select players with heighest scores in descending order. If I were to select n players from each
    team i will select first n players in that chart based on their performance score
    """
    
    marvel_players_performance_chart = sorted(marvel.members, key=player_score, reverse=True)
    dc_players_performance_chart = sorted(dc.members, key= player_score, reverse=True)
    number_of_players = input("enter number of players to be selected: ")
    print("selected marvel players are :",marvel_players_performance_chart[:number_of_players])
    print("selected dc players are :",dc_players_performance_chart[:number_of_players])