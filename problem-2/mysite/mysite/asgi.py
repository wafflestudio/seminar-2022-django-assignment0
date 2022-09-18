import os

from django.core import asgi

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = asgi.get_asgi_application()
