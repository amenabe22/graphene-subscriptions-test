"""
ASGI config for test1 project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/asgi/
"""

import os
import channels
from .consumer import  MyGraphqlWsConsumer
from django.core.asgi import get_asgi_application
from channels.layers import get_channel_layer
from django.urls import path

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test1.settings')

channel_layer = get_channel_layer()
# application = get_asgi_application()

application = channels.routing.ProtocolTypeRouter({
    'websocket': channels.routing.URLRouter([
        path('graphql/', MyGraphqlWsConsumer),
    ])
})