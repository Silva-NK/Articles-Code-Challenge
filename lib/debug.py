# Interactive debugging

from lib.models.author import Author
from lib.models.article import Article
from lib.models.magazine import Magazine

from lib.db.connection import get_connection

author1 = Author(name="Jane Smith")
author1.save()
print(f"Author saved with id = {author1.id} and name = '{author1.name}'")

author2 = Author(name="John Doe")
author2.save()
print(f"Author saved with id = {author2.id} and name = '{author2.name}'")

author3 = Author(name="J Jonah Jameson")
author3.save()
print(f"Author saved with id = {author3.id} and name = '{author3.name}'")

author4 = Author(name="Lois Lane")
author4.save()
print(f"Author saved with id = {author4.id} and name = '{author4.name}'")



mag1 = Magazine(name="Daily Planet", category="Developing Stories")
mag1.save()
print(f"Magazine saved with id = {mag1.id} and name = '{mag1.name}' in category = '{mag1.category}'")

mag2 = Magazine(name="Daily Bugle", category="Creature Clashes")
mag2.save()
print(f"Magazine saved with id = {mag2.id} and name = '{mag2.name}' in category = '{mag2.category}'")

mag3 = Magazine(name="Nat Geo Wild", category="Nature Today")
mag3.save()
print(f"Magazine saved with id = {mag3.id} and name = '{mag3.name}' in category = '{mag3.category}'")



article1 = Article(title="When will we actually address pollution?", author_id=1, magazine_id=1)
article1.save()
print(f"Article saved with id = {article1.id} and title = '{article1.title}' in '{article1.magazine_id}' by '{article1.author_id}'")

article2 = Article(title="What will Spiderman ruin next?", author_id=2, magazine_id=2)
article2.save()
print(f"Article saved with id = {article2.id} and title = '{article2.title}' in '{article2.magazine_id}' by '{article2.author_id}'")

article2 = Article(title="Spiderman. Saviour or Destroyer?", author_id=3, magazine_id=2)
article2.save()
print(f"Article saved with id = {article2.id} and title = '{article2.title}' in '{article2.magazine_id}' by '{article2.author_id}'")

article4 = Article(title="The Masked Streak of Central City?", author_id=3, magazine_id=1)
article4.save()
print(f"Article saved with id = {article4.id} and title = '{article4.title}' in '{article4.magazine_id}' by '{article4.author_id}'")

article5 = Article(title="The extinction of Wildlife", author_id=1, magazine_id=3)
article5.save()
print(f"Article saved with id = {article5.id} and title = '{article5.title}' in '{article5.magazine_id}' by '{article5.author_id}'")



author = Author.find_by_name("J Jonah Jameson")
if author:
    print("-- Articles by J Jonah Jameson --")
    for article in author.articles():
        print(f"{article.id}: {article.title}")
else:
    print("Author not found.")



author = Author.find_by_id(3)
if author:
    print(f"-- Articles by {author.name} --")
    for article in author.articles():
        print(f"{article.id}: {article.title}")

    print(f"-- Magazines {author.name} has written for --")
    for mag in author.magazines():
        print(f"{mag.id}: {mag.name} - {mag.category}")
else:
    print("Author not found.")



mag = Magazine.find_by_name("Daily Bugle")
print(f"-- Authors for {mag.name} --")
for author in mag.authors():
    print(f"{author.id}: {author.name}")



print("-- Magazines with multiple authors --")
magazines = Magazine.mags_with_many_authors()
for mag in magazines:
    print(f"{mag.name} ({mag.category})")



print("-- Article counts per magazine --")
for name, count in Magazine.count_articles():
    print(f"{name} has {count} articles.")



print("-- Leading author by article count --")
author_aficionado, count = Author.author_aficionado()
print(f"Leading author is {author_aficionado.name} with {count} articles.")



article6 = author4.add_article(mag1, "Know your heroes: Connor Kent. Meet Superman's petri dish son.")
print(f"Article saved: {article6.id} - {article6.title}")

article7 = author3.add_article(2, "Inhuman Sightings in Colombia")
print(f"Article saved: {article7.id} - {article7.title}")

article8 = author3.add_article(2, "How do we move now that hero, Quinten Beck, is gone?")
print(f"Article saved: {article8.id} - {article8.title}")



mag = Magazine.find_by_name("Daily Bugle")

print(f"-- Articles in {mag.name} --")
for article in mag.articles():
    print(f"{article.id}: {article.title}")

print(f"\n-- Contributors to {mag.name} --")
for author in mag.contributors():
    print(f"{author.id}: {author.name}")

print(f"\n-- Titles of all articles in {mag.name} --")
for title in mag.article_titles():
    print(f"- {title}")

print(f"\n-- Contributing authors in {mag.name} (more than 2 articles) --")
for author in mag.contributing_authors():
    print(f"{author.id}: {author.name}")



top_mag = Magazine.top_publisher()
if top_mag:
    print(f"Top publisher: {top_mag.name} ({top_mag.category})")
else:
    print("No articles found.")