from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .messages.producer import publish_message
from .models import Sale

app_name = 'dashboard'

def index(request):
    sales = Sale.objects.all()

    # s = sales[0].sale[2:].split(':')[0]
    # dd(s) 

    branches = {
        'matadi': [],
        'goma':[],
        'kisangani':[]
    }

    for item in sales :
        single_sale = item.sale[2:].split(':')
        if (single_sale[0] == 'MA'):
            branches['matadi'].append([single_sale[1],single_sale[2]])

        if (single_sale[0] == 'GO'):
            branches['goma'].append([single_sale[1],single_sale[2]])

        if (single_sale[0] == 'KI'):
            branches['kisangani'].append([single_sale[1],single_sale[2]])

    # dd(branches)

       
    return render(request, 'dashboard/index.html',{
        'sales': branches
    })



def send_message(request):
    branch = request.POST.get('branch', '')
    message = request.POST.get('message', '')

    publish_message((branch+':'+message))

    return HttpResponseRedirect(reverse("dashboard:index"))

