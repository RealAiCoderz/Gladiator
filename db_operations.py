import logger
import model

class DatabaseOperations:
    #creates database initially
    def db_create(self, conn, cursor):
        try:
            cursor.execute("DROP DATABASE IF EXISTS SuperHeroes")
            cursor.execute("CREATE DATABASE SuperHeroes")
            print("Database created. \n")

        except Exception as e:
            logger.make_entry(type(e).__name__)
    
    #populates the database from instances of Star
    def db_populate(self, conn, cursor):
        try:
            cursor.execute("CREATE TABLE Heroes (Name VARCHAR(20) NOT NULL, Height INT NOT NULL, Weight INT NOT NULL, Games_played INT NOT NULL, Team VARCHAR(20) NOT NULL, PRIMARY KEY(Name) );")
            SQL = "INSERT INTO heroes (Name, Height, Weight, Games_played, Team) VALUES (%s, %s, %s, %s, %s)"

            for elem in model.roster:
                row = (elem.get_name(), elem.get_height(), elem.get_weight(), elem.get_games_played(), elem.get_team())
                cursor.execute(SQL, row)
            conn.commit()
            print("Database populated. \n")

        except Exception as e:
            logger.make_entry(type(e).__name__)