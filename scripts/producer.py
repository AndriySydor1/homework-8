import sys
import os

# Додавання кореневого каталогу проекту до шляху пошуку модулів
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pika
import random
from faker import Faker
from mongoengine import connect, Document, StringField

# Підключення до MongoDB
uri = "mongodb+srv://andriysydor91:53rKL6MJXYhePqqA@cluster0.lls6tnz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
connect('contacts_db', host=uri)

faker = Faker()

class Contact(Document):
    fullname = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    preferred_contact_method = StringField(required=True)

def send_to_email_queue(contact_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='email_queue')
    channel.basic_publish(exchange='',
                          routing_key='email_queue',
                          body=json.dumps(contact_data))
    connection.close()

def send_to_sms_queue(contact_data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='sms_queue')
    channel.basic_publish(exchange='',
                          routing_key='sms_queue',
                          body=json.dumps(contact_data))
    connection.close()

def create_contacts(num_contacts):
    contacts = []
    for _ in range(num_contacts):
        contact = Contact(
            fullname=faker.name(),
            phone=faker.phone_number(),
            email=faker.email(),
            preferred_contact_method=random.choice(['email', 'sms'])
        )
        contact.save()
        contact_data = {
            "id": str(contact.id),
            "fullname": contact.fullname,
            "phone": contact.phone,
            "email": contact.email,
            "preferred_contact_method": contact.preferred_contact_method
        }
        if contact.preferred_contact_method == 'email':
            send_to_email_queue(contact_data)
        else:
            send_to_sms_queue(contact_data)
        contacts.append(contact)
    return contacts

if __name__ == "__main__":
    num_contacts = int(input("Enter number of contacts to create: "))
    create_contacts(num_contacts)
    print(f"{num_contacts} contacts created and sent to queues.")

    