from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .messages.producer import publish_message

app_name = 'dashboard'

def index(request):
    return render(request, 'dashboard/index.html')



def send_message(request):
    branch = request.POST.get('branch', '')
    message = request.POST.get('message', '')

    publish_message((branch+':'+message))

    return HttpResponseRedirect(reverse("dashboard:index"))

