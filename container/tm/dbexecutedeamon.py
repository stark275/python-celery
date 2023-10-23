import pika
import mysql.connector

credentials = pika.PlainCredentials('guest', 'guest')
connexion = pika.BlockingConnection(
    pika.ConnectionParameters(
        host='rabbitmq',
        port=5672,
        virtual_host='/',
        credentials=credentials
    )
) 

channel = connexion.channel()
exchange_name = 'erp'
creates_queue = 'eng.created'
create_route_key = 'created'

channel.exchange_declare(exchange_name, durable=True, exchange_type='topic')

channel.queue_declare(queue=creates_queue)
channel.queue_bind(exchange=exchange_name, queue=creates_queue, routing_key=create_route_key)

mydb = mysql.connector.connect(
        host="mysql",
        user="root",
        password="root",    
        database="db"
        # port="33077"
    )


def execute(request):
    # cursor = getDb()
    print(request)

def callback(ch, method, props, body):
    print("[-] Receved: %r" % body)

    clean_query =  str(body)[1:].replace("'","")
    result = clean_query.split("~~~")

    query = result[0].strip('"')
    args = tuple(result[1].strip('[]').strip('"').split(', '))

    # print(query)
    # print(args)

    mycursor = mydb.cursor(prepared=True)
    mycursor.execute(query,args)
    mydb.commit()

    # print(result)
    print(mycursor.rowcount, "success!")

    
channel.basic_consume(
    queue=creates_queue,
    on_message_callback=callback,
    auto_ack=True)

print('[+] Waiting for messages From DBE')

channel.start_consuming() 