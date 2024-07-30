import sys
import os
import json
from models.quote import Quote
from models.author import Author
from utils.db import connect_to_db

# Додавання кореневої теки проекту до шляху пошуку модулів
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

print(f"Project root added to PYTHONPATH: {project_root}")

from models.quote import Quote
from models.author import Author
from utils.db import connect_to_db

# Підключення до бази даних
connect_to_db()
print("Connected to the database.")

# Завантаження цитат з файлу
with open('data/quotes.json', 'r', encoding='utf-8') as f:
    quotes_data = json.load(f)

print(f"Loaded {len(quotes_data)} quotes from the file.")

# Збереження цитат у базу даних
for quote in quotes_data:
    author_name = quote.pop('author')
    author = Author.objects(fullname=author_name).first()
    if author:
        quote['author'] = author
        Quote(**quote).save()
        print(f"Saved quote by: {author_name}")
    else:
        print(f"Author not found for quote: {quote}")

print("All quotes have been saved to the database.")

        