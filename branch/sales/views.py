from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .messages.producer import publish_sale, publish_cash_statment
from .models import Sale, Message
from django.utils import timezone

branch_id = 'MA:'
# Create your views here.

def index(request):
    return render(request, 'sales/index.html')

def sale(request):

    sale_input = request.POST.get('sale', '')

    sale = Sale(sale=sale_input, sale_date=timezone.now())
    sale.save()

    publish_sale(branch_id+sale_input)
  
    return HttpResponseRedirect(reverse("sales:index"))
    

