class Superhero:
    def __init__(self, name, height, weight, games_played):
        self.name = name
        self.height = height
        self.weight = weight
        self.games_played = games_played

    def __str__(self):
        return (f"Superhero(name='{self.name}', height={self.height} cm, "
                f"weight={self.weight} kg, games_played={self.games_played})")


class Team:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, member):
        self.members.append(member)


