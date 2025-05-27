# Magazine class with SQL methods

import sqlite3

from lib.db.connection import get_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self._id = id
        self.name = name
        self.category = category

    
    @property
    def id(self):
        return self._id
    

    @property
    def name(self):
        return self._name
    

    @name.setter
    def name(self, name):
        if not isinstance (name, str) or len(name.strip()) == 0:
            raise ValueError("The Magazine name cannot be an empty string.")
        
        self._name = name.strip()

    
    @property
    def category(self):
        return self._category
    

    @category.setter
    def category(self, category):
        if not isinstance (category, str) or len(category.strip()) == 0:
            raise ValueError("The Magazine category cannot be an empty string.")
        
        self._category = category.strip()

    
    def save(self):
        conn = get_connection()
        cursor = conn.cursor()

        try:
            if self._id is None:
                cursor.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", (self.name, self.category))
                self._id = cursor.lastrowid
            else:
                raise Exception(f"Magazine with ID {self._id} already exists. Save operation stopped.")
            
            conn.commit()

        except sqlite3.IntegrityError as e:
            if "UNIQUE constraint failed: magazines.name" in str(e):
                raise ValueError(f"A magazine with the name '{self.name}' already exists. Please use a unique name.")

        finally:
            conn.close()

        return self
    

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM magazines WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], name=row[1], category=row[2])
        return None


    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM magazines WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], name=row[1], category=row[2])
        return None
    

    @classmethod
    def find_by_category(cls, category):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM magazines WHERE category = ?", (category,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], name=row[1], category=row[2])
        return None
    