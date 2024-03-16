from Marvel import marvel_members
from DC import dc_members
import statistics
from MarvelController import MarvelController
from DCController import DCController

marvelController = MarvelController()
dcController = DCController()
class Probability:
    marvel_members = marvelController.getMarvelMember()
    dc_members = dcController.getDCMember()
    team = marvel_members + dc_members
    total_marvel = len(marvel_members)
    total_dc = len(dc_members)
    total_characters = total_marvel + total_dc
    """=================Level1 Start======================"""
    def calculate_probability1(self):
        print("\n+++++++++++++++++\n")
        # Probability of selecting 2 from Marvel and 3 from DC
        probability_marvel = (self.total_marvel * (self.total_marvel - 1)) / (self.total_characters * (self.total_characters - 1))
        probability_dc = (self.total_dc * (self.total_dc - 1) * (self.total_dc - 2)) / (
                    (self.total_characters - 2) * (self.total_characters - 3) * (self.total_characters - 4))
        print("Probability of selecting 2 from Marvel and 3 from DC:", probability_marvel * probability_dc)
    def filter_character1(self):
        print("\n+++++++++++++++++\n")
        print("All those stars who are heavier than SpiderMan and taller than Henery")
        for character in self.team:
            if character['name'] == "SpiderMan":
                spiderManWeight = character['weight']
            if character['name'] == "Henery":
                heneryHeight = character['height']

        for character in self.team:
            if character['weight'] > spiderManWeight and character['height'] > heneryHeight:
                print(character)
    def filter_character2(self):
        print("\n+++++++++++++++++\n")
        print("All those stars who have played more than 100 games and are heavier than Captain America")
        for character in self.team:
            if character['name'] == "Captain America":
                captainAmerican_weight = character['weight']
        for character in self.team:
            if character['games_played'] > 100 and character['weight'] > captainAmerican_weight:
                print(character)
    def filter_character3(self):
        print("\n+++++++++++++++++\n")
        print("The names of all the stars whose summation of height,weight and games played is greater than 350 units")
        for character in self.team:
            if (character['height'] + character['weight'] + character['games_played'] > 350):
                print(character['name'])

    """=================Level1 End======================"""
    
    """=================Level2 Start======================"""

    def get_heights_weights_gamesPlayed(self):
        heights = [character['height'] for character in self.team]
        weights =[character['weight'] for character in self.team]
        games_played = [character['games_played'] for character in self.team]
        return heights,weights,games_played
    def get_heights_weights(self):
        heights = [character['height'] for character in self.team]
        weights =[character['weight'] for character in self.team]
        return heights,weights
    def find_mean_median(self):
        print("\n+++++++++++++++++\n")
        print("Mean and Median of their respective heights, weights and Games played")
        heights,weights,games_played = self.get_heights_weights_gamesPlayed()
        print(f'Mean:\n \theights :{statistics.mean(heights)} , weights: {statistics.mean(weights)} , games_played: {statistics.mean(games_played)} ')
        print(f'Median:\n \theights :{statistics.median(heights)} , weights: {statistics.median(weights)} , games_played: {statistics.median(games_played)}')

    # Find Deviation and Standard deviation of height and weight.
    def find_deviation(self):
        print("\n+++++++++++++++++\n")
        print("Deviation and Standard deviation of height and weight")
        heights, weights = self.get_heights_weights()
        mean_height,mean_weight = statistics.mean(heights),statistics.mean(weights)
        deviation_heights = [height - mean_height for height in heights]
        deviation_weights = [weight - mean_weight for weight in weights]
        std_deviation_height,std_deviation_weight = statistics.stdev(heights),statistics.stdev(weights)

        print("Deviation\n \tHeights:", ", ".join(f"{deviation_height:.2f}" for deviation_height in deviation_heights))
        print(" \tWeights:", ", ".join(f"{deviation_weight:.2f}" for deviation_weight in deviation_weights))
        print(f"Standard deviation:\n \theights: {std_deviation_height} , weights: {std_deviation_weight}")
    """=================Level2 End======================"""

    """=================Level3 Start======================"""


    def calculate_probability2(self):
        print("\n+++++++++++++++++\n")
        print("If one player is randomly chosen from each team,\nthe probability that both selected players whose height is greater than 180 and played more than 50 games is ",end='')
        selected_marvel_players = [player for player in marvel_members if player['height'] > 180 and player['games_played']>50]
        selected_dc_players = [player for player in dc_members if player['height']>180 and player['games_played'] > 50]
        probability_marvel = len(selected_marvel_players) / len(self.team)
        probability_dc = len(selected_dc_players) / len(self.team)-1
        print(probability_marvel*probability_dc)

    def calculate_probability3(self):
        print("\n+++++++++++++++++\n")
        print("If one player from the Marvel team and two players from the DC team,at least one player selected should have a weight below 80kg\n"
              "the combined weight of the team should not exceed 250 kg")
        marvel_players = [player for player in marvel_members if player['weight'] < 80]
        dc_players = [player for player in dc_members if player['weight'] < 80]
        selected_teams = 0
        for marvel_player in marvel_players:
            for dc_player1 in dc_players:
                for dc_player2 in dc_players:
                    if dc_player1 == dc_player2:
                        continue
                    combined_weight = marvel_player['weight'] + dc_player1['weight'] + dc_player2['weight']
                    if combined_weight <= 250:
                        selected_teams += 1
                        break

        total_possible_teams = len(marvel_players) * len(dc_players) * (len(dc_players) - 1)
        print("Probability of forming such a team:",selected_teams/total_possible_teams)
    """=================Level3 End======================"""
p = Probability()
p.calculate_probability1()
p.filter_character1()
p.filter_character2()
p.filter_character3()
p.find_deviation()
p.calculate_probability2()
p.calculate_probability3()