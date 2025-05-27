# Article class with SQL methods

import sqlite3

from lib.db.connection import get_connection

class Article:
    def __init__(self, id=None, title=None, author_id=None, magazine_id=None):
        self._id = id
        self.title = title
        self.author_id = author_id
        self.magazine_id = magazine_id

    
    @property
    def id(self):
        return self._id
    

    @property
    def title(self):
        return self._title
    

    @title.setter
    def title(self, title):
        if not isinstance (title, str) or len(title.strip()) == 0:
            raise ValueError("The Article title cannot be an empty string.")
        
        self._title = title.strip()

    
    @property
    def author_id(self):
        return self._author_id
    

    @author_id.setter
    def author_id(self, value):
        if not isinstance (value, int) or value <= 0:
            raise ValueError("The Author ID must be a postive integer.")
        
        self._author_id = value
    
    @property
    def magazine_id(self):
        return self._magazine_id
    

    @magazine_id.setter
    def magazine_id(self, value):
        if not isinstance (value, int) or value <= 0:
            raise ValueError("The Magazine ID must be a positive integer.")
        
        self._magazine_id = value


    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self._id is None:
                cursor.execute("INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)", (self.title, self.author_id, self.magazine_id))
                self._id = cursor.lastrowid
            else:
                raise Exception(f"Article with ID {self._id} already exists. Save operation stopped.")
            
            conn.commit()

        finally:
            
            conn.close()

        return self