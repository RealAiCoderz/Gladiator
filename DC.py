dc_members = []
class DC:

    __name = ''
    __height = 0
    __weight = 0
    __games_played = 0
    def setName(self,name):
        self.__name = name
    def getName(self):
        return self.__name
    def setHeight(self,height):
        self.__height = height
    def getHeight(self):
        return self.__height
    def setWeight(self,weight):
        self.__weight = weight
    def getWeight(self):
        return self.__weight
    def setGamesPlayed(self,games_played):
        self.__games_played = games_played
    def getGamesPlayed(self):
        return self.__games_played