import sys
import os
import json

# Додавання кореневої теки проекту до шляху пошуку модулів
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

print(f"Project root added to PYTHONPATH: {project_root}")

from models.author import Author
from utils.db import connect_to_db

# Підключення до бази даних
connect_to_db()
print("Connected to the database.")

# Завантаження авторів з файлу
with open('quotes_scraper/data/new_authors.json', 'r', encoding='utf-8') as f:
    authors_data = json.load(f)

print(f"Loaded {len(authors_data)} authors from the file.")

# Список полів, які повинні бути в моделі Author
allowed_fields = {'fullname', 'born_date', 'born_location', 'description'}

# Збереження авторів у базу даних
for author in authors_data:
    if 'fullname' not in author or not author['fullname']:
        print(f"Skipping author due to missing fullname: {author}")
        continue

    filtered_author = {key: value for key, value in author.items() if key in allowed_fields}
    Author(**filtered_author).save()
    print(f"Saved author: {filtered_author['fullname']}")

print("All authors have been saved to the database.")
    
    