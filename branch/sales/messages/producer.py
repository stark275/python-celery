import pika

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
channel.queue_declare(queue='vente')

def publish_sale(body):
    channel.basic_publish(
        exchange='', routing_key='vente', body=str(body))
    
def publish_cash_statment(body):
    channel.basic_publish(
        exchange='', routing_key='caisse', body=str(body))
