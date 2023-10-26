from django.shortcuts import render
from django.utils import timezone
from .models import *
from .tasks import *
from django.db import connection
from django.http import JsonResponse
from celery.result import AsyncResult
import ast

# Create your views here.

def index(request):
    
    # student = Student(name='Test Insert FABRICE', crated_at=timezone.now())
    # student.save()
    # st = Student.objects.all()
    # dd(st)

    celery_tasks = []

    for i in range(3):
        result = add.delay(i)
        # Créer un objet AsyncResult avec l'ID de la tâche
        # async_result = AsyncResult(result.task_id)

        celery_tasks.append(result.task_id)

    # for query in connection.queries:
    #     print(query['sql'])
    # Soumission des tâches à la file d'attente
    # results = [add.delay(i) for i in range(100)]
    # # Suivi de la progression
    # while not all(result.ready() for result in results):
    #     completed = sum(result.ready() for result in results)
    #     print(f"Progress: {completed}%")
    #     time.sleep(1)

    # dd('LOL')

    return render(request, 'studentModule/index.html',{
        'tasks': celery_tasks
    })

def get_task_info(request):
    task_ids = request.POST.get('task_ids', None)

    tasks = ast.literal_eval(task_ids)

    # print(tasks[0])
    if isinstance(tasks, list):
        print("C'est une liste") 
    elif isinstance(tasks, str):
        print("C'est une chaîne de caractères") 
    done_tasks = []
    if tasks is not None:
        for id in tasks:
            if isDone(id):
                done_tasks.append(id)
        return JsonResponse({'done_tasks': done_tasks})
    else:
        return JsonResponse({'error': 'No task_id in the request'})


def isDone(task_id):
    task = AsyncResult(task_id)
    print(task_id)
    print(task.state)
    print(task.result)
    print(task.ready())

    if task.ready(): 
        return True
    return False
