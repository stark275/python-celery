import pika


def check_read_query( string):
    keywords = ['insert', 'update', 'delete']
    return any(string.lower().startswith(k) for k in keywords)

def dont_contain_django_tables(string):
    array = [
        "`auth_group`",
        "`auth_group_permissions`", 
        "`auth_permission`",
        "`auth_user`",
        "`auth_user_groups`",
        "`auth_user_user_permissions`",
        "`django_admin_log`",
        "`django_content_type`",
        "`django_migrations`",
        "`django_session`",
        # "`studentModule_student`"
    ]

    string_words = string.split()
    print(string_words)
    for word in string_words:
        if word in array:
            return False
    return True


class SQLBrokerPublisher:
    def __init__(self):
        # fichier Env pour credentials
        self.credentials = pika.PlainCredentials('guest', 'guest')
        self.connexion = None
        self.ensure_connection()

    def ensure_connection(self):
        if not self.connexion or self.connexion.is_closed:
            self.connexion = pika.BlockingConnection(
                # fichier Env pour les parametres
                pika.ConnectionParameters(
                    host='rabbitmq',
                    port=5672,
                    virtual_host='/',
                    credentials=self.credentials,
                    heartbeat=600  #  Battement de cœur
                )
            )

    def bublish(self, query, args=None):
        try:
            # args is None means no string interpolation .
            if(check_read_query(query) and dont_contain_django_tables(query)): 
                self.ensure_connection()
                channel = self.connexion.channel()

                exchange_name = 'erp'
                creates_queue = 'eng.created'
                create_route_key = 'created'

                channel.exchange_declare(exchange_name, durable=True, exchange_type='topic')

                channel.queue_declare(queue=creates_queue)
                channel.queue_bind(exchange=exchange_name, queue=creates_queue, routing_key=create_route_key)

                message = ''
                if isinstance(args, list):
                    args = tuple(args)
                
                message = str(query)+'~~~'+str(args)
                channel.basic_publish(
                    exchange=exchange_name,
                    routing_key=create_route_key,
                    body=message)
                print('[--------BEGIN FROM SQLBrokerPublish-------]')
                print(query)
                print('[--------END FROM SQLBrokerPublish---------]')

                # print('[--------BEGIN FROM SQLBrokerPublish-------]')
                # print(self.connexion )
                # print('[--------END FROM SQLBrokerPublish---------]')


                return any
            
        except Exception as e:
            print(f"Erreur lors de l'exécution de la requête : {e}")
            self.close()  # Fermer la connexion en cas d'erreur

    def close(self):
        if self.connexion and not self.connexion.is_closed:
            self.connexion.close()  # Méthode pour fermer la connexion lorsque vous avez terminé
