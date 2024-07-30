import sys
import os

# Додавання кореневої теки проекту до шляху пошуку модулів
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
if project_root not in sys.path:
    sys.path.append(project_root)

print(f"Project root added to PYTHONPATH: {project_root}")
print(f"Current sys.path: {sys.path}")

from models.quote import Quote
from models.author import Author
from utils.db import connect_to_db

# Підключення до бази даних
connect_to_db()
print("Connected to the database.")

def search_by_author(name):
    author = Author.objects(fullname__icontains=name).first()
    if not author:
        print(f"No author found with name: {name}")
        return
    quotes = Quote.objects(author=author)
    for quote in quotes:
        print(quote.quote)

def search_by_tag(tag):
    quotes = Quote.objects(tags__icontains=tag)
    for quote in quotes:
        print(quote.quote)

def search_by_tags(tags):
    tag_list = tags.split(',')
    quotes = Quote.objects(tags__in=tag_list)
    for quote in quotes:
        print(quote.quote)

def main():
    while True:
        command = input("Enter a command (name:author, tag:tag, tags:tag1,tag2, exit): ")
        if command.startswith("name:"):
            search_by_author(command[len("name:"):])
        elif command.startswith("tag:"):
            search_by_tag(command[len("tag:"):])
        elif command.startswith("tags:"):
            search_by_tags(command[len("tags:"):])
        elif command == "exit":
            break
        else:
            print("Unknown command")

if __name__ == "__main__":
    main()
    