"""WSGI config for webservice.
"""

# Stdlib imports
import os

# Django and DRF imports
from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings")

application = get_wsgi_application()
