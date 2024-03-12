class SuperheroView:
    def display_team(self, team):
        print(f"\n{team.name} Team:")
        for member in team.members:
            print(f"Name: {member.name}, Height: {member.height} cm, "
                  f"Weight: {member.weight} kg, Games Played: {member.games_played}")
