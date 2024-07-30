import sys
import os

# Додавання кореневого каталогу проекту до шляху пошуку модулів
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import json
import pika
from mongoengine import connect, Document, StringField

# Логування
def log(message):
    print(f"[LOG]: {message}")

log("Starting consumer_sms.py")

# Підключення до MongoDB
uri = "mongodb+srv://andriysydor91:53rKL6MJXYhePqqA@cluster0.lls6tnz.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
log(f"Connecting to MongoDB at {uri}")
connect('contacts_db', host=uri)
log("Connected to MongoDB")

class Contact(Document):
    fullname = StringField(required=True)
    phone = StringField(required=True)
    email = StringField(required=True)
    preferred_contact_method = StringField(required=True)

def callback(ch, method, properties, body):
    log("Received a message from sms_queue")
    contact_data = json.loads(body)
    log(f"Message data: {contact_data}")
    print(f"Sending SMS to {contact_data['phone']}")
    if 'id' in contact_data:
        contact = Contact.objects.get(id=contact_data['id'])
        print(f"SMS sent to {contact.fullname}")
    else:
        print("Received data does not contain 'id' field")
    ch.basic_ack(delivery_tag=method.delivery_tag)
    log("Message processed and acknowledged")

log("Connecting to RabbitMQ")
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
log("Connected to RabbitMQ")
channel = connection.channel()
channel.queue_declare(queue='sms_queue')
log("Declared sms_queue")

channel.basic_consume(queue='sms_queue', on_message_callback=callback)
log('Waiting for messages. To exit press CTRL+C')
channel.start_consuming()

