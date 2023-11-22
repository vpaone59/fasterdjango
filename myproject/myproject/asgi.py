"""
ASGI config for myproject project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application
from fastapi import FastAPI

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "myproject.settings")

application = get_asgi_application()

from myapp.views import router


def get_application() -> FastAPI:
    app = FastAPI()
    app.include_router(router)
    return app


app = get_application()
