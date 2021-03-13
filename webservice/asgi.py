"""ASGI config for webservice.
"""

# Stdlib imports
import os

# Django and DRF imports
from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings")

application = get_asgi_application()
