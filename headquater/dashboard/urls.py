from django.urls import path
from . import views

app_name = 'dashboard'
urlpatterns = [
    # ex: /dashboard/
    path("", views.index, name="index"),
    path("send-message/", views.send_message, name="send_message"),
]