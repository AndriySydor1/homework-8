import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from mongoengine import connect
from quotes_scraper.models import Author, Quote
import json
import os

# Підключення до вашої MongoDB
connect('myDatabase', host='mongodb+srv://andriysydor91:53rKL6MJXYhePqqA@cluster0.lls6tnz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0')

def load_data_from_json(file_path, model):
    with open(file_path, 'r', encoding='utf-8') as file:  # Додано encoding='utf-8'
        data = json.load(file)
        for item in data:
            obj = model(**item)
            obj.save()

# Базовий шлях до проекту
base_dir = os.path.dirname(os.path.abspath(__file__))

# Завантаження даних в колекції
load_data_from_json(os.path.join(base_dir, '../quotes_scraper/data/new_authors.json'), Author)
load_data_from_json(os.path.join(base_dir, '../quotes_scraper/data/new_quotes.json'), Quote)
