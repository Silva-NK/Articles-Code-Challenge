# Interactive debugging

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

from lib.db.connection import get_connection

author = Author(name="Jane Smith")
author.save()
print(f"Author saved with id={author.id} and name='{author.name}'")