import pika
import django
import os
from django.utils import timezone

from pathlib import Path
import sys 

sys.path.append(
    os.path.join(os.path.dirname(__file__), 'branch')
)
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "branch.settings")

from django.conf import settings

from sales.models import Message

# current_path = os.path.abspath(os.path.dirname(__file__))
# parent_path = Path(current_path)
# settings = str(parent_path.parent.parent.absolute())+'/branch/settings.py'

# print(settings)

# path.append(settings) #Your path to settings.py file
# # os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings') 
# django.setup()


credentials = pika.PlainCredentials('l1fasi', '123456789')
connexion = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='localhost',
        port=5672,
        virtual_host='parallel_programming',
        credentials=credentials
    )
)

channel = connexion.channel()



def get_messages(ch, method, properties, body):

    message = Message(content=str(body), sale_date=timezone.now() )
    message.save()

    print("[-] Receved: %r" % body)

channel.basic_consume(queue='matadi', on_message_callback=get_messages, auto_ack=True)
print("Started Consuming...")

channel.start_consuming()