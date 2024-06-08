from __init__ import conn,cursor
class Author:
    
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    def add_to_database(self):
        sql = """"
            INSERT INTO authors (id,name) VALUES (?)
        """
        params = (self.name,)

        cursor.execute(sql,params)
        conn.commit()

        self.id = cursor.lastrowid


        
