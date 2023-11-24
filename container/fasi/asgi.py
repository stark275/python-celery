import os
import sys
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ErpProject.settings')

sys.path.append("/var/www/ErpDgtcp")
django_application = get_asgi_application()

from . import urls # noqa isort:skip

application = ProtocolTypeRouter(
    {
        "http": get_asgi_application(),
        "websocket": URLRouter(urls.websocket_urlpatterns) #
    }
)


