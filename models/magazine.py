from database.connection import get_db_connection

class Magazine:
    def __init__(self, id, name, category):
        self._id = id
        self.name = name
        self.category = category
        self.conn = get_db_connection()
        self.cursor = self.conn.cursor()

    def __repr__(self):
        return f'<Magazine {self.name}>'
    
    def add_magazine_to_database(self):
        sql = """
            INSERT INTO magazines (name,category) VALUES(?,?)
    """
        params = (self.name,self.category)
        self.cursor.execute(sql,(params))
        self.conn.commit()

        self.id = self.cursor.lastrowid

    @property
    def id(self):
        return self._id
    
    @id.setter
    def id(self,value):
        if not isinstance(value,int):
            raise TypeError("ID must be an integer")
        self._id = value