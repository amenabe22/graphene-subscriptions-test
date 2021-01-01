"""
WSGI config for test1 project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/howto/deployment/wsgi/
"""

import os
import channels
from django.urls import path
from .consumer import MyGraphqlWsConsumer
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'test1.settings')

# application = get_wsgi_application()
application = channels.routing.ProtocolTypeRouter({
    'websocket': channels.routing.URLRouter([
        path('graphql/', MyGraphqlWsConsumer),
    ])
})
