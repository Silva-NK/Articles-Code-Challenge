# Script to set up the database

from lib.db.connection import get_connection

def apply_schema():
    print("Applying schema...")
    conn = get_connection()
    with open('lib/db/schema.sql', 'r') as f:
        sql = f.read()
    conn.executescript(sql)
    conn.commit()
    conn.close()
    print("Schema applied!")

if __name__ == "__main__":
    apply_schema()