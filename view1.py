from model import TeamMember
from controller1 import TeamController

class TeamView:
    
    def input_team_member(team_name):
        while True:
            try:
                name = input(f"Enter {team_name} team member name: ")
                height = TeamController.get_valid_input("Enter height (175 to 205 cm): ", 175, 205)
                weight = TeamController.get_valid_input("Enter weight (75 to 140 kg): ", 75, 140)
                games_played = TeamController.get_valid_input("Enter games played: ", 0, float('inf'))
                return TeamMember(name, height, weight, games_played)
            except ValueError as ve:
                print(f"Invalid input. {ve}")