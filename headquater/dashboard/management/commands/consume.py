import pika
from django.utils import timezone

from django.core.management.base import BaseCommand, CommandError
from ...models  import  Sale

class Command(BaseCommand):
   
    def handle(self, *args, **options):

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

        channel.basic_consume(queue='sales', on_message_callback=self.get_sales, auto_ack=True)
        
        self.stdout.write(
                self.style.SUCCESS("Started Consuming...1")
            )
        channel.start_consuming()
        
    def get_sales(ch, method, properties, body, b):
        sale = Sale(sale=str(b), sale_date=timezone.now() )
        sale.save()
        
        print("[-] Receved: %r" % b)

        
