import sqlite3
import pandas as pd
import logging
logging.basicConfig(filename='database.log', level=logging.INFO, format='%(asctime)s %(username)s %(session_id)s %(message)s')

def create_connection(database_name):
    """Create a connection to the SQLite database."""
    conn = sqlite3.connect(database_name)
    return conn

def create_table(conn):
    """Create the desired table in the database."""
    cursor = conn.cursor()
    
    table_creation_query = '''
    CREATE TABLE IF NOT EXISTS metaverse (
        name TEXT NOT NULL ,
        universe TEXT NOT NULL,
        weight FLOAT NOT NULL,
        height FLOAT NOT NULL,
        games_played INTEGER NOT NULL,
        PRIMARY KEY (name,universe)
    );
    '''


    cursor.execute(table_creation_query)
    conn.commit()

def close_connection(conn):
    """Close the connection to the database."""
    conn.close()

def insert_data(db_name, user_name,session_id,name, universe, height,weight,games_played):
        try:
            conn = create_connection(db_name)
            cursor = conn.cursor()
            insert_query = '''
            INSERT INTO metaverse (name, universe, height,weight,games_played) VALUES (?, ?, ?, ? ,?);
            '''
            cursor.execute(insert_query, (name, universe, height,weight,games_played))
            conn.commit()
            logging.info(f"Data inserted: {name} {universe}", extra={'username': user_name, 'session_id': session_id})

        except sqlite3.IntegrityError as e:
            print(f"Superhero {name} from {universe} already exists in the database.")
            conn.rollback()
            logging.error(f"Error occurred: {e}", extra={'username': user_name, 'session_id': session_id})

        except Exception as e:
            print(e)
            conn.rollback()
            logging.error(f"Error occurred: {e}", extra={'username': user_name, 'session_id': session_id})
        finally:
            close_connection(conn)

def fetch_record(db_name, user_name,session_id,name, universe):
    try:
        conn = create_connection(db_name)
        cursor = conn.cursor()
        if universe:
            select_query = '''
            SELECT * FROM metaverse WHERE name = ? AND universe = ?;
            '''
            cursor.execute(select_query, (name, universe))
        else:
            select_query = '''
            SELECT * FROM metaverse WHERE name = ?;
            '''
            cursor.execute(select_query, (name,))
        data = cursor.fetchone()
        if data:
            logging.info(f"Data fetched: {name} {universe}", extra={'username': user_name, 'session_id': session_id})
            return data
        else:
            logging.error(f"Data not found: {name} {universe}", extra={'username': user_name, 'session_id': session_id})
            return None
    except Exception as e:
        logging.error(f"Error occurred: {e}", extra={'username': user_name, 'session_id': session_id})
        return None
    finally:
        close_connection(conn)
    
def update_record(db_name, user_name,session_id,superhero):
    try:
        conn = create_connection(db_name)
        cursor = conn.cursor()
        update_query = '''
        UPDATE metaverse
        SET name = ?,
            universe = ?,
            height = ?,
            weight = ?,
            games_played = ?
        WHERE name = ? AND universe = ?;
        '''
        cursor.execute(update_query, (superhero.get_name(), superhero.get_universe(),superhero.get_height(), superhero.get_weight(), superhero.get_games_played(), superhero.get_name(), superhero.get_universe()))
        conn.commit()
        logging.info(f"Data updated: {superhero.get_name()} {superhero.get_universe()}", extra={'username': user_name, 'session_id': session_id})

    except Exception as e:
        print(e)
        logging.error(f"Error occurred: {e}", extra={'username': user_name, 'session_id': session_id})
        return None
    finally:
        close_connection(conn)
    
def delete_record(db_name, user_name,session_id,superhero):
    name = superhero.get_name()
    universe = superhero.get_universe()
    try:
        conn = create_connection(db_name)
        cursor = conn.cursor()
        delete_query = '''
        DELETE FROM metaverse WHERE name = ? AND universe = ?;
        '''
        cursor.execute(delete_query, (name, universe))
        conn.commit()
        logging.info(f"Data deleted: {name} {universe}", extra={'username': user_name, 'session_id': session_id})
    except Exception as e:
        logging.error(f"Error occurred: {e}", extra={'username': user_name, 'session_id': session_id})
        return None
    finally:
        close_connection(conn)

def table_to_df(conn):
    sql_query = "SELECT * FROM metaverse;"
    df = pd.read_sql(sql_query, conn)
    return df

def calculate_statistics(db_name, user_name, session_id):
    conn = create_connection(db_name)
    df = table_to_df(conn)
    close_connection(conn)
    if len(df) == 0:
        print("No data in the table")
        return None
    statistics = df.describe()
    print(statistics)
    logging.info(f"Statistics calculated: {statistics}", extra={'username': user_name, 'session_id': session_id})
    return 
    
if __name__ == "__main__":
    database_name = 'metaverse.db'
    conn = create_connection(database_name)
    create_table(conn)
    close_connection(conn)
    