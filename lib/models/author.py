# Author class with SQL methods

from lib.db.connection import get_connection

class Author:
    def __init__(self, id=None, name=None):
        self._id = id
        self.name = name

    
    @property
    def id(self):
        return self._id


    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, name):
        if not isinstance (name, str) or len(name.strip()) == 0:
            raise ValueError("The Author name cannot be an empty string.")
        
        self._name = name.strip()

    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self._id is None:
                cursor.execute("INSERT INTO authors (name) VALUES (?)", (self.name,))
                self._id = cursor.lastrowid
            else:
                raise Exception(f"Author with ID {self._id} already exists. Save operation stopped.")
            conn.commit()
        finally:
            conn.close()

        return self