#
# Model
class Superhero:
    def __init__(self, name, weight, height,universe,games_played):
        self.__name = name
        self.__weight = weight
        self.__height = height
        self.__universe = universe
        self.__games_played = games_played
    
    # write getter setter for each of the attributes
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight

    def get_height(self):
        return self.__height

    def set_height(self, height):
        self.__height = height

    def get_universe(self):
        return self.__universe

    def set_universe(self, universe):
        self.__universe = universe
    # set getter and setter for games_played
    def get_games_played(self):
        return self.__games_played
    
    def set_games_played(self, games_played):
        self.__games_played = games_played

    def __str__(self):
        return f"{self.__name} ({self.__weight} kg, {self.__height} m) from {self.__universe} played {self.__games_played} games"
    

