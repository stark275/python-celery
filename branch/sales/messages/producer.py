import pika

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

channel.exchange_declare('operations', durable=True, exchange_type='topic')
channel.queue_declare(queue= 'sales')
channel.queue_bind(exchange='operations', queue='sales', routing_key='sales')

def publish_sale(body):
    channel.basic_publish(
        exchange='', routing_key='sales', body=str(body))
    
def publish_cash_statment(body):
    channel.basic_publish(
        exchange='', routing_key='cash_statement', body=str(body))
