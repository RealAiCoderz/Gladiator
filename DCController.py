from DC import DC ,dc_members
from DCView import DCView
from Connector import Connector
dc_team = DC()

db = Connector()
class DCController:
    def dcInput(self):
        try:
            name = input("Enter member's name: ")
            dc_team.setName(name)
            while True:
                height = float(input("Enter member's height between 175 and 205 cm: "))
                if 175 <= height <= 205:
                    dc_team.setHeight(height)
                    break
                else:
                    print("Height must be between 175 and 205.")

            while True:
                weight = float(input("Enter member's weight between 75 and 140 kg: "))
                if 75 <= weight <= 140:
                    dc_team.setWeight(weight)
                    break
                else:
                    print("Weight must be between 75 and 140.")
            games_played = int(input("Enter number of games played: "))
            dc_team.setGamesPlayed(games_played)
            return {'name': dc_team.getName(), 'height': dc_team.getHeight(), 'weight': dc_team.getWeight(), 'games_played': dc_team.getGamesPlayed()}

        except ValueError:
            print("Invalid Type")
    def addMember(self,n):
        i = 0
        while i<n:
            member = self.dcInput()
            db.dbConnection(member, "dc_team")
            dc_members.append(member)
            i = i+1

    def getDCMember(self):
        rows =db.retreiveFromDB("dc_team")
        for row in rows:
            # Convert each row to a dictionary for easy access
            data_dict = {
                "name": row[0],
                "height": row[1],
                "weight": row[2],
                "games_played": row[3]
            }
            dc_members.append(data_dict)
        return dc_members

# team = DCController()
# team.addMember(2)
# team.getDCMember()
# view = DCView()
# view.display()
