import time
from celery import shared_task
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
from django.utils import timezone
from .models import *

@shared_task
def add(i):
    for j in range(3):
        time.sleep(0.1) # Simuler un travail
        # self.update_state(state='PROGRESS', meta={'current': j, 'total': 100})

    return i*i

@shared_task
def create_student_task(name):
    
    print('LLOOOOOOLLLL CELERY')
    student = Student(name=name, crated_at=timezone.now())
    student.save()
    student_id =  student.id 

    async def async_func():
        # Obtenez la couche de canal
        channel_layer = get_channel_layer()
        # Envoyez le message au groupe de l'utilisateur
        await channel_layer.group_send(
            "asynch_sql",
            {
                'type': 'send_notification',
                'message': "[Student ID] ->  " + str(student_id),   
            }
        )
    # Exécutez la coroutine et obtenez le résultat
    async_to_sync(async_func)()

@shared_task
def notify(user_id, message):

    async def async_func(user_id, message):
        # Obtenez la couche de canal
        channel_layer = get_channel_layer()

        
        # Envoyez le message au groupe de l'utilisateur
        await channel_layer.group_send(
            "asynch_sql",
            {
                'type': 'send_notification',
                'message': f"[Ce message est important] {message}"
            }
        )

    # Exécutez la coroutine et obtenez le résultat
    return async_to_sync(async_func)(user_id, message)

    