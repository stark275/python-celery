from django.shortcuts import render

app_name = 'dashboard'

def index(request):
    return render(request, 'dashboard/index.html')

def send_message(request):
    return False
