import time
from celery import shared_task

@shared_task
def add(i):
    for j in range(3):
        time.sleep(0.1) # Simuler un travail
        # self.update_state(state='PROGRESS', meta={'current': j, 'total': 100})

    return i*i
