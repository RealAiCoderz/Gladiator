import sqlite3
from model import Superhero
from db_functions import insert_data, fetch_record, update_record, delete_record, calculate_statistics
import re
import uuid
from view import SuperheroView

# Controller
class SuperheroController:
    __admin_users = set(['kt6269'])
    def __init__(self):
        self.__view = SuperheroView()
        self.__session_id = uuid.uuid4()
        self.__user = None
    
    def start(self):
        user_id = input("Welcome to the Superhero Database. Please Enter your userid to continue (Enter 'q' to quit): ")
        if user_id == 'q':
            print("Exiting the program.")
            return
        while not self.validate_user(user_id):
            user_id = input("Please enter a valid user id (Enter 'q' to quit): ")
            if user_id == 'q':
                print("Exiting the program.")
                return
        return self.options()
    
    def options(self):
        print("1. Create a superhero")
        print("2. View a superhero")
        print("3. Update a superhero")
        print("4. Delete a superhero")
        print("5. calculate mean,mode and standard deviation of columns")
        print("6. Exit")
        choice = input("Enter your choice (digit 1 to 6): ")
        while choice not in ['1', '2', '3', '4', '5','6']:
            print("Invalid choice. Please enter a valid choice.")
            choice = input("Enter your choice: ")
        if choice == '1':
            self.create_superhero()
            return self.options()
        elif choice == '2':
            self.view_superhero()
            return self.options()
        elif choice == '3':
            self.update_superhero()
            return self.options()
        elif choice == '4':
            self.delete_superhero()
            return self.options()
        elif choice == '5':
            calculate_statistics('metaverse.db',self.__user,self.__session_id)
            return self.options()
        elif choice == '6':
            print("Exiting the program.")
            return


    def create_superhero(self):
        name = input("Enter the name of the superhero: ")
        universe = input("Enter the universe of the superhero: ")
        weight = input("Enter the weight of the superhero: ")
        height = input("Enter the height of the superhero: ")
        games_played = input("Enter the number of games played by the superhero: ")
        if not self.validate_superhero_info(name, weight, height, universe, games_played):
            return self.create_superhero()
        superhero = Superhero(name, weight, height,universe,games_played)
        self.save_superhero(superhero)
        self.__view.display(superhero)

    def save_superhero(self, superhero):
        insert_data('metaverse.db',self.__user,self.__session_id,superhero.get_name(), superhero.get_universe(), superhero.get_height(),superhero.get_weight(),superhero.get_games_played())
        return
    
    def view_superhero(self):
        name = input("Enter the name of the superhero: ")
        universe = input("Enter the universe of the superhero: ")
        data = fetch_record('metaverse.db',self.__user,self.__session_id,name, universe)
        # Add code to display the superhero data
        if data:
            superhero = Superhero(data[0], data[3], data[2], data[1], data[4])
            self.__view.display(superhero)
        else:
            print("Superhero not found.")

    def update_superhero(self):
        name = input("Enter the name of the superhero: ")
        universe = input("Enter the universe of the superhero: ")
        data = fetch_record('metaverse.db',self.__user,self.__session_id,name, universe)
        if data:
            superhero = Superhero(data[0], data[3], data[2], data[1], data[4])
            self.__view.display(superhero)
            weight = input("Enter the new weight of the superhero: ")
            height = input("Enter the new height of the superhero: ")
            games_played = input("Enter the new number of games played by the superhero: ")
            #if not self.validate_superhero_info(superhero.get_name(), weight, height, superhero.get_universe(), games_played):
            #    return self.update_superhero()
            if weight:
                superhero.set_weight(weight)
            if height:
                superhero.set_height(height)
            if games_played:
                superhero.set_games_played(games_played)
            update_record('metaverse.db',self.__user,self.__session_id,superhero)
            self.__view.display(superhero)
        else:
            print("Superhero not found.")
        
    def delete_superhero(self):
        print('Admin users:',SuperheroController.__admin_users)
        print('Current user:',self.__user)
        if self.__user not in SuperheroController.__admin_users:
                print('Non-Admin user not authorized to DELETE superhero')
                return
        name = input("Enter the name of the superhero: ")
        universe = input("Enter the universe of the superhero: ")
        data = fetch_record('metaverse.db',self.__user,self.__session_id,name, universe)
        if data:
            superhero = Superhero(data[0], data[3], data[2], data[1], data[4])
            delete_record('metaverse.db',self.__user,self.__session_id,superhero)

        else:
            print("Superhero not found.")

        
    def validate_user(self, user_id):
        pattern = r"^(?=.*[a-zA-Z])(?=.*\d)[a-zA-Z\d]{2,10}$"
        if re.match(pattern, user_id):
            # User ID is valid
            # Add your code here
            self.__user = user_id
            return True
        else:   
            # User ID is invalid
            # Add your code here
            print('Invalid user ID. Please enter a valid user ID. User ID should be 2-10 characters long and should contain at least one letter and one number.')
            return False
            
    def validate_superhero_info(self, name, weight, height, universe, games_played):
        if not name.isalpha():
            print("Invalid name. Name should contain only alphabets.")
            return False

        if not universe.isalpha():
            print("Invalid universe. Universe should contain only alphabets.")
            return False

        try:
            float(weight)
        except ValueError:
            print("Invalid weight. Weight should be a float or integer.")
            return False

        try:
            float(height)
        except ValueError:
            print("Invalid height. Height should be a float or integer.")
            return False

        try:
            int(games_played)
        except ValueError:
            print("Invalid number of games played. Number of games played should be an integer.")
            return False

        return True
        

