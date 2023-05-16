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


# Connection a l'exchange appelé message, qui est durable et qui a le type topic
channel.exchange_declare('message', durable=True, exchange_type='topic')

channel.queue_declare(queue= 'matadi')

# Attache de la queue A à l'échange message, avec l'utlisation de la clef de routage A
channel.queue_bind(exchange='message', queue='matadi', routing_key='matadi')

# Création d'une queue appelée B
channel.queue_declare(queue= 'goma')
# Attache de la queue B à l'échange message, avec l'utlisation de la clef de routage B
channel.queue_bind(exchange='message', queue='goma', routing_key='goma')

# Création d'une queue appelée RFI
channel.queue_declare(queue= 'kisangani')
# Attache de la queue C à l'échange message, avec l'utlisation de la clef de routage C
channel.queue_bind(exchange='message', queue='kisangani', routing_key='kisangani')

branchs = {'matadi', 'goma', 'kisangani'}

def publish_message(message):
    for br in branchs:
        channel.basic_publish(
                    exchange='message',
                    routing_key=br,
                    body=message )
            

    