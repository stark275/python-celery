from django.shortcuts import render
from django.utils import timezone
from .models import *
from .tasks import *
from django.db import connection

from .tasks_progession import *
# Create your views here.

def profile(request):
    return render(request, 'studentModule/profile.html')

def index(request):
    
    # student = Student(name='Test Insert FABRICE', crated_at=timezone.now())
    # student.save()
    # st = Student.objects.all()
    # dd(st)

    celery_tasks = []

    for i in range(200):
        result = add.delay(i)
        celery_tasks.append(result.task_id)


    request.session['payment_tasks'] = []

    lot_id = 80

    add_new_payment_group(request,{
        "payment_lot" : lot_id,
        "payment_ids" : celery_tasks,
        "task_count" : len(celery_tasks),
        "show_progress" : True
    })
    
    
    vd(request.session['payment_tasks'])


    return render(request, 'studentModule/index.html',{
        'tasks': celery_tasks,
        'lot_id': lot_id
    })

