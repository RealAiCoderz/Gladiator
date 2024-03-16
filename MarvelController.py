from Marvel import Marvel,marvel_members
from MarvelView import MarvelView
from Connector import Connector
marvel_team = Marvel()


db = Connector()
class MarvelController:
    def marvelInput(self):
        try:
            name = input("Enter member's name: ")
            marvel_team.setName(name)
            while True:
                height = float(input("Enter member's height between 175 and 205 cm: "))
                if 175 <= height <= 205:
                    marvel_team.setHeight(height)
                    break
                else:
                    print("Height must be between 175 and 205.")

            while True:
                weight = float(input("Enter member's weight between 75 and 140 kg: "))
                if 75 <= weight <= 140:
                    marvel_team.setWeight(weight)
                    break
                else:
                    print("Weight must be between 75 and 140.")
            games_played = int(input("Enter number of games played: "))
            marvel_team.setGamesPlayed(games_played)
            return {'name': marvel_team.getName(), 'height': marvel_team.getHeight(), 'weight': marvel_team.getWeight(), 'games_played': marvel_team.getGamesPlayed()}

        except ValueError:
            print("Invalid Type")
    def addMember(self,n):
        i = 0
        while i<n:
            member = self.marvelInput()
            db.dbConnection(member, "marvel_team")
            marvel_members.append(member)
            i = i+1

    def getMarvelMember(self):
        rows =db.retreiveFromDB("marvel_team")
        for row in rows:
            # Convert each row to a dictionary for easy access
            data_dict = {
                "name": row[0],
                "height": row[1],
                "weight": row[2],
                "games_played": row[3]
            }
            marvel_members.append(data_dict)
        return marvel_members

team = MarvelController()
team.addMember(1)
# team.getMarvelMember()
# view = MarvelView()
# view.display()
