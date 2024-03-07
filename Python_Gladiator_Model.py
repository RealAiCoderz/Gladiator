import logging
import mysql.connector
from mysql.connector import Error
import numpy as np

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

#Represents a member of a team
class TeamMember:
    def __init__(self, name, height, weight, games_played):
        self.name = name
        self.height = height
        self.weight = weight
        self.games_played = games_played

'''Inserts a member's data into a MySQL database table. 
If an error occurs during database insertion, it's logged using the Python logging module.'''
class Team:
    def __init__(self, name):
        self.name = name
        self.members = np.empty((0, 4), dtype=object)

    def add_member(self, member):
        if len(self.members) >= 20:
            logging.warning(f"Team {self.name} is already full with 20 members.")
        else:
            self.members = np.append(self.members, [[member.name, member.height, member.weight, member.games_played]], axis=0)

    def insert_member_to_db(self, member):
        try:
            connection = mysql.connector.connect(host='localhost',
                                                 database='MyDB',
                                                 user='root',
                                                 password='Root123@')
            if connection.is_connected():
                cursor = connection.cursor()
                table_name = self.name.lower()
                query = f"INSERT INTO {table_name} (Name, Height, Weight, Games_Played) VALUES (%s, %s, %s, %s)"
                data = (member.name, member.height, member.weight, member.games_played)
                cursor.execute(query, data)
                connection.commit()
                logging.info(f"Inserted member {member.name} into {table_name} table")
        except Error as e:
            logging.error(f"Error inserting member data into {self.name} table: {e}")
        finally:
            if connection.is_connected():
                cursor.close()
                connection.close()
