# Makes controllers a package

from lib.db.connection import get_connection

def add_author_with_articles(author_name, articles_data):

    conn = get_connection()
    try:
        with conn:
            cursor = conn.cursor()

            cursor.execute(
                "INSERT INTO authors (name) VALUES (?) RETURNING id",
                (author_name,)
            )
            author_id = cursor.fetchone()[0]

            for article in articles_data:
                cursor.execute(
                    "INSERT INTO articles (title, author_id, magazine_id) VALUES (?, ?, ?)",
                    (article['title'], author_id, article['magazine_id'])
                )

        return True

    except Exception as e:
        print(f"Transaction failed: {e}")
        return False
