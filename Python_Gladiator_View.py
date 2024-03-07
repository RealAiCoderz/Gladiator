#View Module

import numpy as np
from Python_Gladiator_Model import TeamMember

class View:
    #Takes a message as input and prompts the user to enter input based on the message.
    def get_input(self, message):
        return input(message)

    #Prints a given message to the console for display purposes.
    def display_message(self, message):
        print(message)

    '''Prompts the user to enter details for a new team member.
    It ensures that the name entered contains only alphabetic characters and 
    validates the height and weight inputs using the get_valid_input method.'''
    def get_member_data(self, team_name):
        from Python_Gladiator_Controller import Controller
        print(f"\nEnter details for the new member in Team {team_name}:")
        while True:
            name = input("Name: ")
            if name.isalpha() and name.strip():
                break
            else:
                print("Invalid name. Please enter a valid name containing only alphabetic characters.")
        height = self.get_valid_input("Height (cm): ", self.validate_height)
        weight = self.get_valid_input("Weight (kg): ", self.validate_weight)
        games_played = int(input("Games Played: "))
        return TeamMember(name, height, weight, games_played)

    #Prompts the user to enter input based on the message and validates the input using a provided validator function.
    def get_valid_input(self, message, validator):
        while True:
            try:
                value = int(input(message))
                if not validator(value):
                    raise ValueError(f"Invalid input. {message}")
                return value
            except ValueError as ve:
                print(ve)

    #Validates the height input to ensure it falls within the range
    def validate_height(self, height):
        return 175 <= height <= 205

    # Validates the weight input to ensure it falls within the range
    def validate_weight(self, weight):
        return 75 <= weight <= 140

    #Displays updated data for a given team
    def display_team_data(self, team):
        print(f"\nUpdated Data for Team {team.name}:")
        print("Name\tHeight (cm)\tWeight (kg)\tGames Played")
        for member in team.members:
            print("\t".join(str(x) for x in member))
