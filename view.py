class View:

    def disp(self, cursor, SQL):
        cursor.execute(SQL)
        result = cursor.fetchall()
        
        return result