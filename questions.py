
from sklearn.linear_model import LinearRegression
from view1 import TeamView
from controller1 import TeamController
from model import Team

try:
    # Create Marvel and DC teams
    marvel = Team("Marvel")
    dc = Team("DC")

    # Assumption: Storing 3 members in each team
    for i in range(3):
        marvel.add_member(TeamView.input_team_member("Marvel"))

    for i in range(3):
        dc.add_member(TeamView.input_team_member("DC"))

    # Query 1.1
    prob = TeamController.probability_of_selection(marvel, dc, 2, 3)
    print(f"\nProbability of selecting 2 from Marvel and 3 from DC teams: {prob}")

    # Query 1.2
    heavier_taller_players = TeamController.find_heavier_taller_players(marvel, dc, spiderman_weight=75, henery_height=176)
    print("Stars heavier than SpiderMan and taller than Henery:", heavier_taller_players)

    # Query 1.3
    players_more_than_100_games = TeamController.find_players_more_than_games_and_heavier_than(
        marvel, dc, games_threshold=100, captainamerica_weight=85)
    print("Stars who have played more than 100 games and are heavier than Captain America:", players_more_than_100_games)

    # Query 1.4
    metaverse_stars = TeamController.find_metaverse_stars(marvel, dc)
    print("Stars for the metaverse with stats summation greater than 350 units:", metaverse_stars)

  
    # Statistical calculations
    heights = [member.height for member in marvel.members + dc.members]
    weights = [member.weight for member in marvel.members + dc.members]
    games_played = [member.games_played for member in marvel.members + dc.members]

    # Query 2.1
    mean_height = TeamController.calculate_mean(heights)
    median_height = TeamController.calculate_median(heights)
    print(f"\nMean Height: {mean_height}, Median Height: {median_height}")

    # Query 2.2
    mean_weight = TeamController.calculate_mean(weights)
    median_weight = TeamController.calculate_median(weights)
    print(f"Mean Weight: {mean_weight}, Median Weight: {median_weight}")

    # Query 2.3
    mean_games_played = TeamController.calculate_mean(games_played)
    median_games_played = TeamController.calculate_median(games_played)
    print(f"Mean Games Played: {mean_games_played}, Median Games Played: {median_games_played}")

    # Query 2.4
    deviation_heights = TeamController.calculate_deviation(heights, mean_height)
    deviation_weights = TeamController.calculate_deviation(weights, mean_weight)
    print(f"Deviation of Heights: {deviation_heights}")
    print(f"Deviation of Weights: {deviation_weights}")

    # Query 2.5
    standard_deviation_heights = TeamController.calculate_standard_deviation(heights, mean_height)
    standard_deviation_weights = TeamController.calculate_standard_deviation(weights, mean_weight)
    print(f"Standard Deviation of Heights: {standard_deviation_heights}")
    print(f"Standard Deviation of Weights: {standard_deviation_weights}")

    # Prepare data for linear regression
    X = [[member.weight] for member in marvel.members + dc.members]
    y = [member.games_played for member in marvel.members + dc.members]

    # Create and fit the model
    model = LinearRegression()
    model.fit(X, y)

    # linear regression model
    print(f"Linear Regression Model: y = {model.coef_[0]} * x + {model.intercept_}")

   
except Exception as e:
    print(f"An error occurred: {e}")
    
