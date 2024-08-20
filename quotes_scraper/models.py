from mongoengine import Document, StringField, ListField, ReferenceField

class Author(Document):
    name = StringField(required=True, max_length=200)  # Оновлено з fullname на name
    birth_date = StringField(max_length=100)  # Оновлено з born_date на birth_date
    birth_place = StringField(max_length=200)  # Оновлено з born_location на birth_place
    description = StringField()

class Quote(Document):
    tags = ListField(StringField(max_length=50))
    author = ReferenceField(Author, reverse_delete_rule=2)
    text = StringField(required=True, max_length=2000)  # Збільшено максимальну довжину
