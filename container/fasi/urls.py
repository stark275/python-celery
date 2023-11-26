
from django.contrib import admin
from django.urls import path, include, re_path
from studentModule.consumer import SQLBrokerExecConsumer

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('studentModule.urls')),
]

websocket_urlpatterns = [
    path('ws/sql/<int:user_id>/', SQLBrokerExecConsumer.as_asgi()),
    # re_path(r"ws/db-write/(?P<user_id>(0|[1-9]\d*))/$", DBWriteConsumer.as_asgi()),
]
