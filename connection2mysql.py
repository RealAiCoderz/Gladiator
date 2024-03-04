import mysql.connector
import logging
import time

# Configure logging with time
log_format = '%(asctime)s - %(levelname)s - %(message)s'
logging.basicConfig(filename='databasemain.log', level=logging.INFO, format=log_format)

try:
    # Establish a connection to the MySQL database
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Sana123!",
        database="project_main"
    )

    cursor = connection.cursor()

    # Create a table for team members if it doesn't exist
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS team_members (
            id INT AUTO_INCREMENT PRIMARY KEY,
            team_name VARCHAR(255),
            member_name VARCHAR(255),
            height INT,
            weight INT,
            games_played INT
        )
    """)

    connection.commit()

    # Prompt user for data
    team_name = input("Enter team name: ")
    member_name = input("Enter member name: ")
    height = int(input("Enter height: "))
    weight = int(input("Enter weight: "))
    games_played = int(input("Enter games played: "))

    # Insert data into the table
    cursor.execute("""
        INSERT INTO team_members (team_name, member_name, height, weight, games_played)
        VALUES (%s, %s, %s, %s, %s)
    """, (team_name, member_name, height, weight, games_played))

    connection.commit()

    logging.info("Data inserted successfully.")

except mysql.connector.Error as mysql_error:
    logging.error(f"MySQL Error: {mysql_error}")
    print(f"Error interacting with MySQL database: {mysql_error}")

except Exception as e:
    logging.error(f"Error: {e}")
    print(f"An unexpected error occurred: {e}")

finally:
    # Close the database connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        logging.info("MySQL connection closed.")