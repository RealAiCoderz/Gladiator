import logging
from Aiview import SuperheroView
from Aimod import Team, Superhero
from itertools import combinations

class SuperheroController:
    def __init__(self):
        self.logger = logging.getLogger(__name__)

    def validate_input(self, value, min_value, max_value):
        while True:
            try:
                user_input = float(input(f"Enter {value} ({min_value} - {max_value}): "))
                if min_value <= user_input <= max_value:
                    return user_input
                else:
                    print(f"{value} should be between {min_value} and {max_value}. Try again.")
            except ValueError:
                print(f"Invalid input for {value}. Please enter a valid number.")

    def create_superhero(self):
        try:
            name = input("Enter superhero name: ")
            height = self.validate_input("height", 175, 205)
            weight = self.validate_input("weight", 75, 140)
            games_played = int(input("Enter number of games played: "))
            return Superhero(name, height, weight, games_played)
        except Exception as e:
            self.logger.error(f"Error creating superhero: {e}")
            raise

logging.basicConfig(level=logging.INFO)

# Main program
marvel_team = Team("Marvel")
dc_team = Team("DC")
controller = SuperheroController()
view = SuperheroView()

# Add members to Marvel team
for _ in range(5):
    try:
        member = controller.create_superhero()
        marvel_team.add_member(member)
    except Exception as e:
        print(f"Error adding Marvel team member: {e}")

# Add members to DC team
for _ in range(5):
    try:
        member = controller.create_superhero()
        dc_team.add_member(member)
    except Exception as e:
        print(f"Error adding DC team member: {e}")

# Display teams
view.display_team(marvel_team)
view.display_team(dc_team)

marvel_selection_count = 2
dc_selection_count = 1
# question-1
# Calculate the total number of combinations for Marvel and DC teams
marvel_combinations = list(combinations(marvel_team.members, marvel_selection_count))
dc_combinations = list(combinations(dc_team.members, dc_selection_count))

# Calculate the total number of possible outcomes
total_outcomes = len(marvel_combinations) * len(dc_combinations)

# Assuming all members are equally likely to be selected, each outcome has the same probability
probability_of_selection = 1 / total_outcomes

print(f"Total outcomes: {total_outcomes}")
print(f"Probability of selecting 2 members from Marvel and 1 member from DC: {probability_of_selection}")
