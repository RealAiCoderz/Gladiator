import mysql.connector
import logging
class Connector:
    def dbConnection(self,member,team_name):
        try:
            con = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="admin123",
                database="AITraining"
            )
            print("connect to database")
            logging.basicConfig(filename="project.log",encoding="utf-8",level=logging.DEBUG)
            logging.info("connect to database")
            mydb = con.cursor()
            query = "INSERT INTO {} (name, height, weight, games_played) VALUES (%s, %s, %s, %s)".format(team_name)
            mydb.execute(query, (member['name'], member['height'], member['weight'], member['games_played']))
            con.commit()
            print("Team members  inserted successfully.")
            logging.info("Team members  inserted successfully.")
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)
            logging.error("Error connecting to MySQL database:")
    def retreiveFromDB(self,team_name):
        try:
            con = mysql.connector.connect(
                host="127.0.0.1",
                user="root",
                password="admin123",
                database="AITraining"
            )
            print("connect to database")
            mydb = con.cursor()
            query = "SELECT * FROM {}".format(team_name)
            mydb.execute(query)
            rows = mydb.fetchall()
            mydb.close()
            con.close()
            # print("Team members are retrieved successfully.")
            return rows
        except mysql.connector.Error as e:
            print("Error connecting to MySQL database:", e)

