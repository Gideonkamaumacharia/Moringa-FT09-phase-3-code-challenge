import sqlite3

class Author:
    def __init__(self, id, name):
        self.id = id
        self.name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    def add_to_database(self):
        conn = sqlite3.connect('./database/magazine.db')
        cursor = conn.cursor()

        cursor.execute("""INSERT INTO authors (id,name) VALUES (?,?)""",(self.id,self.name))
        cursor.fetchone()

        conn.commit()
        conn.close()

new_author = Author(1,"John Doe")