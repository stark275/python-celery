from django.urls import path
from . import views

app_name = 'studentModule'
urlpatterns = [
    # ex: /students/
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path('get-task-info/', views.get_task_info, name='get_task_info'),

    # path("sale/", views.sale, name="sale"),
] 