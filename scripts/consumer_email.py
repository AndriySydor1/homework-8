import sys
import os

# Додавання кореневого каталогу проекту до шляху пошуку модулів
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pika
from mongoengine import connect, Document, StringField

# Підключення до MongoDB
uri = "mongodb+srv://andriysydor91:53rKL6MJXYhePqqA@cluster0.lls6tnz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connect('contacts_db', host=uri)

class Contact(Document):
    fullname = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    preferred_contact_method = StringField(required=True)

def callback(ch, method, properties, body):
    contact_data = json.loads(body)
    print(f"Sending email to {contact_data['fullname']} at {contact_data['email']}")
    contact = Contact.objects.get(id=contact_data['id'])
    print(f"Email sent to {contact.fullname}")
    ch.basic_ack(delivery_tag=method.delivery_tag)

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='email_queue')

channel.basic_consume(queue='email_queue', on_message_callback=callback)
print('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()
