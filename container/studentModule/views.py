from django.shortcuts import render
from django.utils import timezone
from .models import *
from django.db import connection


# Create your views here.

def index(request):
    
    student = Student(name='Test Insert Via Broker Requests', crated_at=timezone.now())
    student.save()
    st = Student.objects.all()
    dd(st)

    # for query in connection.queries:
    #     print(query['sql'])

    # dd(connection.queries)



    return render(request, 'studentModule/index.html')
