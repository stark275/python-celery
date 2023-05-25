## Bases de rabbitMQ
[RabbitMQ](https://blog.eleven-labs.com/fr/rabbitmq-partie-1-les-bases/)

## RabbitMQ Lien entre Channel et connection
[RabbitMQ: Channels et connetions](
https://www.cloudamqp.com/blog/the-relationship-between-connections-and-channels-in-rabbitmq.html?gclid=CjwKCAjw6vyiBhB_EiwAQJRoplOhLkGd6gyt2L9YhnCuIX8a9HWgjxmq9-f2vnj-3D6FMSj6DSOrrhoCjAQQAvD_BwE)


## Le problème avec une Queue ayant plusieurs Consumers
[Une queue ](https://stackoverflow.com/questions/10620976/rabbitmq-amqp-single-queue-multiple-consumers-for-same-message)

## Videos: Configuger python et pika
[Partie 1](https://youtu.be/eSN0otKzYOE)
[Partie 2](https://youtu.be/Wiw7oOgBjFs)

## Django + Celery + rabbitMQ
[Configuration 1](https://simpleisbetterthancomplex.com/tutorial/2017/08/20/how-to-use-celery-with-django.html)

[Configuration 2 (Vu pendant les TP)](https://dontrepeatyourself.org/post/asynchronous-tasks-in-django-with-celery-and-rabbitmq/)

[Avec recuperation des résultats après un traitement d'un worker Celery](https://github.com/stark275/python-celery/blob/main/headquater/dashboard/management/commands/consume.py)

## Communication entre deux applications django via RabbitMQ

[Communication inter-instance](https://www.section.io/engineering-education/communicating-between-your-django-apis-using-rabbitmq/)

## Créer une commande personnalisée avec Django
Comme vu pendant le cours lorsqu'on veut consommer un message et l'afficher sur une page
est peu faisable via une vue Django. L'une des piste de solution c'est de créer une commande personnalisée qui va se charger d'ecouter rabbitMQ en continue, consommer les messages, les enregistrer dans la base de donnée pour enfin les afficher. [Comme dans le TP ici](https://github.com/stark275/python-celery/blob/main/headquater/dashboard/management/commands/consume.py)

Docummentation officielle:
[Custom command](https://docs.djangoproject.com/fr/4.2/howto/custom-management-commands/)

Conteneuriser une application Django

[Docker + Django 1](https://medium.com/backticks-tildes/how-to-dockerize-a-django-application-a42df0cb0a99)

[Docker + Django 2](https://blog.logrocket.com/dockerizing-django-app/)