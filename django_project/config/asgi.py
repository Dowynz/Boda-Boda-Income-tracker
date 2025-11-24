import os
from channels.routing import ProtocolTypeRouter, URLRouter
from django.core.asgi import get_asgi_application
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')
django.setup()
from django.urls import path, re_path, include
from chat import routing as chat_routing
from call import routing as call_routing
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": URLRouter(chat_routing.websocket_urlpatterns + call_routing.websocket_urlpatterns),
})
