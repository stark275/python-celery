from django.urls import path
from . import views, tasks_progession

app_name = 'studentModule'
urlpatterns = [
    # ex: /students/
    path("", views.index, name="index"),
    path("profile/", views.profile, name="profile"),
    path('get-task-info/', tasks_progession.get_task_info, name='get_task_info'),
    path('send/', views.send_message, name='send_message'),

    path('create-student/', views.create_student, name='create_student'),

    # path("sale/", views.sale, name="sale"),
] 