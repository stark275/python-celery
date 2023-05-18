import pika
from django.utils import timezone

from django.core.management.base import BaseCommand, CommandError
from ...models  import Message, Sale

class Command(BaseCommand):
   
    def handle(self, *args, **options):

        credentials = pika.PlainCredentials('l1fasi', '123456789')
        connexion = pika.BlockingConnection(
            pika.ConnectionParameters(
                host='localhost',
                port=5672,
                virtual_host='parallel_programming',
                credentials=credentials,
                heartbeat=600,
                blocked_connection_timeout=300
            )
        )

        channel = connexion.channel()

        channel.basic_consume(queue='matadi', on_message_callback=self.get_messages, auto_ack=True)
        self.stdout.write(
                self.style.SUCCESS("Started Consuming....")
            )
        channel.start_consuming()
        
    def get_messages(ch, method, properties, body, b):
        message = Message(content=str(b), pub_date=timezone.now() )
        message.save()
        
        print("[-] Receved: %r" % b)

        
