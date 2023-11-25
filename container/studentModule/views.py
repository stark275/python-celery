from django.http import HttpResponse
from django.shortcuts import render
from django.utils import timezone
from .models import *
from .tasks import *
from django.db import connection

from .tasks_progession import *
# Create your views here.

# CHANNELS FOR ASYNC SYSTEM
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
import asyncio
from channels.http import AsgiRequest

async def send_message(request):
	print("CHANNEL")

	message = request.GET.get('message', None)
	channel_layer = get_channel_layer()

	await channel_layer.group_send(
		"asynch_sql",
		{
			"type": "send_notification",
			"message": message,
		}
	)
     
	return HttpResponse("Message sent!")

def create_student(request):
    if request.method == 'POST':
        # Recevoir les données POST de manière asynchrone
        name = request.POST.get('name')

        create_student_task.delay(name)


   
    return HttpResponse("Message sent!")

def profile(request):
    return render(request, 'studentModule/profile.html')

def index(request):
    
    # student = Student(name='Test Insert FABRICE', crated_at=timezone.now())
    # student.save()
    # st = Student.objects.all()
    # dd(st)

    # celery_tasks = []

    # for i in range(200):
    #     result = add.delay(i)
    #     celery_tasks.append(result.task_id)


    # request.session['payment_tasks'] = []

    # lot_id = 89

    # add_new_payment_group(request,{
    #     "payment_lot" : lot_id,
    #     "payment_ids" : celery_tasks,
    #     "task_count" : len(celery_tasks),
    #     "show_progress" : True
    # })
    
    
    vd(request.session['payment_tasks'])


    return render(request, 'studentModule/index.html',{
        'tasks': [],
        'lot_id': 1
    })

