# Interactive debugging

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

from lib.db.connection import get_connection

author1 = Author(name="Jane Smith")
author1.save()
print(f"Author saved with id = {author1.id} and name = '{author1.name}'")


mag1 = Magazine(name="Daily Planet", category="Developing Stories")
mag1.save()
print(f"Magazine saved with id = {mag1.id} and name = '{mag1.name}' in category = '{mag1.category}'")


article1 = Article(title="When will we actually address pollution?", author_id=1, magazine_id=1)
article1.save()
print(f"Article saved with id = {article1.id} and title = '{article1.title}' in '{article1.magazine_id}' by '{article1.author_id}'")