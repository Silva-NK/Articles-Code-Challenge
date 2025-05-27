# Author class with SQL methods

import sqlite3

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
    

    @classmethod
    def find_by_id(cls, id):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM authors WHERE id = ?", (id,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], name=row[1])
        return None
    

    @classmethod
    def find_by_name(cls, name):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM authors WHERE name = ?", (name,))
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], name=row[1])
        return None
    

    def articles(self):
        from lib.models.article import Article
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(""" SELECT * FROM articles WHERE author_id = ? """, (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [Article(id=row[0], title=row[1], author_id=row[2], magazine_id=row[3]) for row in rows]
    

    def magazines(self):
        from lib.models.magazine import Magazine
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(""" 
                       SELECT DISTINCT m.* 
                       FROM magazines m JOIN articles a ON m.id = a.magazine_id 
                       WHERE a.author_id = ? ORDER BY m.id ASC
                       """, (self.id,))
        rows = cursor.fetchall()
        conn.close()

        return [Magazine(id=row[0], name=row[1], category=row[2]) for row in rows]
    

    @classmethod
    def author_aficionado(cls):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(""" SELECT a.id, a.name, COUNT(ar.id) as article_count FROM authors a
                       JOIN articles ar ON a.id = ar.author_id 
                       GROUP BY a.id LIMIT 1;
                       """)
        
        row = cursor.fetchone()
        conn.close()

        if row:
            return cls(id=row[0], name=row[1]), row[2]
        return None, 0
    

    def add_article(self, magazine, title):
        from lib.models.article import Article
        from lib.models.magazine import Magazine

        if isinstance(magazine, Magazine):
            magazine_id = magazine.id
        elif isinstance(magazine, int):
            magazine_id = magazine
        else:
            raise ValueError("Magazine must be a Magazine instance or an integer ID.")
        
        article = Article(title=title, author_id=self.id, magazine_id=magazine_id)
        article.save()
        return article
    

    def topic_areas(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute(""" SELECT DISTINCT m.category FROM magazines m
                       JOIN articles a ON m.id = a.magazine_id
                       WHERE a.author_id = ?
                       """, (self.id,))
        
        categories = [row[0] for row in cursor.fetchall()]
        conn.close()

        return categories