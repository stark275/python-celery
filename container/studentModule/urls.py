from django.urls import path
from . import views

app_name = 'studentModule'
urlpatterns = [
    # ex: /students/
    path("", views.index, name="index"),

    # path("sale/", views.sale, name="sale"),
] 