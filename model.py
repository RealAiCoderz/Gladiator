roster = []

#each instance of Star is a superhero
class Star:
    __name = None
    __height = None
    __weight = None
    __games_played = None
    __team = None
    
    def __init__(self):
        pass
    
    # setter methods
    def set_name(self, n):
        self.name = n
    
    def set_height(self, h):
        self.height = h
    
    def set_weight(self, w):
        self.weight = w
    
    def set_games_played(self, gp):
        self.games_played = gp
    
    def set_team(self, t):
        self.team = t
    
    # getter methods
    def get_name(self):
        return(self.name)
    
    def get_height(self):
        return(self.height)
    
    def get_weight(self):
        return(self.weight)
    
    def get_games_played(self):
        return(self.games_played)
    
    def get_team(self):
        return(self.team)