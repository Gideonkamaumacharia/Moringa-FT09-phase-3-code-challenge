from database.connection import get_db_connection


class Author:
    
    def __init__(self, id, name):
        self._id = id
        self._name = name
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def __repr__(self):
        return f'<Author {self.name}>'
    
    
    def add_to_database(self):
        sql = """"
            INSERT INTO authors (name) VALUES (?)
        """
        params = (self._name,)

        self.cursor.execute(sql,params)
        self.conn.commit()

        self.id = self.cursor.lastrowid

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
        cls.cursor.execute(sql,(id,))
        result = cls.cursor.fetchone()
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




        
