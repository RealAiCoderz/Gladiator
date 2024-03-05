import mysql.connector

class Connection:
    def make_connection(self, db_name=None):
        try:
            conn = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "gd#3lfE2f",
            database = db_name
            )
        except Exception as e:
            print(type(e).__name__, e)
        else:
            cursor = conn.cursor()
            # return connection and cursor objects
            return (conn, cursor)
