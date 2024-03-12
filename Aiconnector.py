import logging

import mysql.connector
import logging
from Aimod import Superhero

class SuperheroDatabase:
    def __init__(self, host, user, password, database):
        self.host = host
        self.user = user
        self.password = password
        self.database = database
        self.connection = None
        self.logger = logging.getLogger(__name__)

    def connect(self):
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.logger.info("Connected to the MySQL database.")
        except Exception as e:
            self.logger.error(f"Error connecting to the MySQL database: {e}")
            raise

    def create_tables(self):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS superheroes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    name VARCHAR(255),
                    height FLOAT,
                    weight FLOAT,
                    games_played INT
                )
            ''')
            self.connection.commit()
        except Exception as e:
            self.logger.error(f"Error creating tables: {e}")
            raise

    def insert_superhero(self, superhero):
        try:
            cursor = self.connection.cursor()
            cursor.execute('''
                INSERT INTO superheroes (name, height, weight, games_played)
                VALUES (%s, %s, %s, %s)
            ''', (superhero.name, superhero.height, superhero.weight, superhero.games_played))
            self.connection.commit()
        except Exception as e:
            self.logger.error(f"Error inserting superhero into the MySQL database: {e}")
            raise

    def fetch_superheroes(self):
        try:
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM superheroes")
            superheroes = cursor.fetchall()
            return superheroes
        except Exception as e:
            self.logger.error(f"Error fetching superheroes from the MySQL database: {e}")
            raise

    def close_connection(self):
        if self.connection:
            self.connection.close()
            self.logger.info("Connection to the MySQL database closed.")

# Usage example
if __name__ == "__main__":
    # Configure logging
    logging.basicConfig(level=logging.INFO)

    # MySQL connection parameters (replace these with your MySQL server details)
    host = "localhost"
    user = "root"
    password = "Pintu123@"
    database = "super_heroes"

    # Create a SuperheroDatabase instance and establish a connection
    db = SuperheroDatabase(host, user, password, database)
    db.connect()

    # Create tables if they don't exist
    db.create_tables()

    # Main program:
    iron_man = Superhero("Iron Man", 185, 85, 100)
    spider_man = Superhero("Spider Man", 175, 70, 80)
    thor = Superhero("thor", 187, 120, 75)
    captain_America = Superhero("captain America", 184, 85, 205)
    Hulk = Superhero("Hulk", 175, 70, 80)
    batman = Superhero("Batman", 180, 85, 105)
    Superman = Superhero("Superman", 189, 95, 305)
    Harvedent = Superhero("Harvedent", 181, 75, 55)
    henery = Superhero("henery", 176, 87, 125)
    Heralt = Superhero("Heralt", 184, 100, 145)

    # Insert Superheroes into the MySQL database
    db.insert_superhero(iron_man)
    db.insert_superhero(spider_man)
    db.insert_superhero(thor)
    db.insert_superhero(captain_America)
    db.insert_superhero(Hulk)
    db.insert_superhero(batman)
    db.insert_superhero(Superman)
    db.insert_superhero(Harvedent)
    db.insert_superhero(henery)
    db.insert_superhero(Heralt)

    # Close the MySQL database connection
    db.close_connection()



