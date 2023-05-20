from django.urls import path
from . import views

app_name = 'sales'
urlpatterns = [
    # ex: /sales/
    path("", views.index, name="index"),

    path("sale/", views.sale, name="sale"),
] 