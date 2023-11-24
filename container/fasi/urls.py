
from django.contrib import admin
from django.urls import path, include
from studentModule.consumer import SQLBrokerExecConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('studentModule.urls')),
]

websocket_urlpatterns = [
    path("ws/sql/", SQLBrokerExecConsumer.as_asgi())
]
