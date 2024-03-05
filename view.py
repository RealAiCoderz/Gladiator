
def disp(cursor, SQL):
    cursor.execute(SQL)
    result = cursor.fetchall()
    
    return result