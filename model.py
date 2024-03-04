class TeamMember:
    def __init__(self, name, height, weight, games_played):
        self.name = name
        self.height = height
        self.weight = weight
        self.games_played = games_played

class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)