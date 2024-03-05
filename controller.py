import logger
import custom_exceptions

import model
from connection import Connection
from db_operations import DatabaseOperations as db
from view import View
import level_1_questions as level1

log = logger.Logger()

#get character information from 'char_data.txt' into instances of Star
with open("char_data.txt", 'r', encoding='utf-8') as file:  
    line = file.readline()
    while (line):
        #acquire each row as list and clean it.
        details = line.split(",")
        details = [item.strip("\n ") for item in details]
        details[1:4] = map(int, details[1:4])
        
        #validation of height and weight. Currently does not stop program execution
        if not (175<= details[1] <=205):
            try:
                raise custom_exceptions.HeightError
            except custom_exceptions.HeightError as e:
                log.make_entry("HeightError (given {} for {})".format(details[1], details[0]))
        
        if not (75<= details[2] <=140):
            try:
                raise custom_exceptions.WeightError
            except custom_exceptions.WeightError as e:
                log.make_entry("WeightError (given {} for {})".format(details[2], details[0]))
        
        #One Star instance for each row
        star = model.Star()
        
        star.set_name(details[0])
        star.set_height(details[1])
        star.set_weight(details[2])
        star.set_games_played(details[3])
        star.set_team(details[4])
        
        #add instance to roster
        model.roster.append(star)
        
        line = file.readline()

#-------Create Schema-------
conn, cursor = Connection().make_connection()
db().db_create(conn, cursor)
conn.close()

#-------Populate database-------
conn, cursor = Connection().make_connection(db_name = "SuperHeroes")
db().db_populate(conn, cursor)

#-------Do level 1 questions-------
'''
1. pass cursor and sql query string to disp() of View class.
2. will get database result in return.
3. pass above result as input to q1/q2/etc. to make calculations and print answer.
'''
level1.q1(View().disp(cursor, level1.q1_sql))
level1.q2(View().disp(cursor, level1.q2_sql))
level1.q3(View().disp(cursor, level1.q3_sql))
level1.q4(View().disp(cursor, level1.q4_sql))

conn.close()

#-------another small example exception handling and logging
try:
    print(a) # 'a' does not exist
except NameError as e:
    log.make_entry(type(e).__name__)

logger.f.close()