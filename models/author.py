from __init__ import conn,cursor
class Author:
    
    def __init__(self, id, name):
        self._id = id
        self._name = name

    def __repr__(self):
        return f'<Author {self.name}>'
    
    def create_tables(self):
         cursor.execute('''
        CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    
    def add_to_database(self):
        sql = """"
            INSERT INTO authors (id,name) VALUES (?)
        """
        params = (self._name,)

        cursor.execute(sql,params)
        conn.commit()

        self.id = cursor.lastrowid

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        if not isinstance(value,int):
            raise ValueError("ID should be an integer")
        self._id = value
    
    @classmethod
    def from_database(cls,id):
        sql = """
            SELECT name 
            FROM authors 
            WHERE id = ?
    """
        cursor.execute(sql,(id,))
        result = cursor.fetchone()
        if result:
            return cls(id,result[0])
        else:
            raise ValueError(f"Author with ID {id} not found in database ")
        
        

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        if isinstance(value,str) and len(value) > 0:
            if not hasattr(self, "_name") or self._name is None:
                self._name = value
            else:
                raise AttributeError("Name cannot be changed after instantiation")
        else:
            raise ValueError("Name shouldnt be an empty string")




        
