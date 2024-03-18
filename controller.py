from model import Member,Team
import view
import sqlite3
import logging

logging.basicConfig(filename='team_log.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
class SupesController():
    try:
        conn = sqlite3.connect('team_database.db')
        c = conn.cursor()
        c.execute('''CREATE TABLE IF NOT EXISTS marvel (
                        name TEXT,
                        height INTEGER,
                        weight INTEGER,
                        games_played INTEGER
                    )''')

        c.execute('''CREATE TABLE IF NOT EXISTS dc (
                        name TEXT,
                        height INTEGER,
                        weight INTEGER,
                        games_played INTEGER
                    )''')
    except sqlite3.Error as e:
        logging.error(f"Error connecting to database: {e}")
        
    marvel = Team("Marvel")
    dc = Team("DC")
    all_members = []
    weights=[]
    heights=[]
    games_played_list=[]
    ans = ""
    try:
        while ans.upper()!='N':
            name = input("Enter member name: ")
            height = view.get_valid_input("Enter height (175-205 cm): ", 175, 205)
            weight = view.get_valid_input("Enter weight (75-140 kg): ", 75, 140)
            games_played = view.get_valid_input("Enter number of games played: ", 0, float('inf'))
            member = Member(name, height, weight, games_played)
            all_members.append(member)
            team_choice = input("Add to Marvel (M) or DC (D) team? ").upper()
            if team_choice == "M":
                marvel.add_member(member)
                c.execute("INSERT INTO marvel VALUES (?, ?, ?, ?)", (name, height, weight, games_played))
            elif team_choice == "D":
                dc.add_member(member)
                c.execute("INSERT INTO dc VALUES (?, ?, ?, ?)", (name, height, weight, games_played))
            else:
                print("Invalid team choice. Member not added.")
            weights.append(weight)
            heights.append(height)
            games_played_list.append(games_played)
            ans = input("Do you want to add more Entries: Y or N:  ")
    except Exception as e:
        logging.error(f"Error adding member: {e}")
    try:
        conn.commit()
        conn.close()
    except sqlite3.Error as e:
        logging.error(f"Error committing changes and closing connection: {e}")