#Controller Module

import logging
from Python_Gladiator_Model import Team, TeamMember
from Python_Gladiator_View import View

class Controller:
    #Initializes an instance of the View class to interact with the user.
    def __init__(self):
        self.marvel_team = Team("Marvel")
        self.dc_team = Team("DC")
        self.view = View()

    #Prompts the user to add members to a specified team
    def add_member_to_team(self, team):
        max_attempts = 3
        while len(team.members) < 20:
            choice = self.view.get_input(f"Do you want to add a member to Team {team.name}? (yes/no): ")
            if choice.lower().startswith("y"):
                member = self.view.get_member_data(team.name)
                team.add_member(member)
                team.insert_member_to_db(member)
            elif choice.lower().startswith("n"):
                break
            else:
                self.view.display_message("Invalid input. Please enter 'yes' or 'no'.")
                max_attempts -= 1
                if max_attempts == 0:
                    self.view.display_message("Maximum attempts reached. Exiting.")
                    break

    '''It calls add_member_to_team for both the Marvel and DC teams, 
    and then displays the team data using the display_team_data method of the View class.'''
    def run(self):
        self.add_member_to_team(self.marvel_team)
        self.add_member_to_team(self.dc_team)
        self.view.display_team_data(self.marvel_team)
        self.view.display_team_data(self.dc_team)

if __name__ == "__main__":
    logging.info("Starting program")

    controller = Controller()
    controller.run()

    logging.info("Program finished")

