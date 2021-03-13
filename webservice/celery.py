"""Celery config file
https://docs.celeryproject.org/en/stable/django/first-steps-with-django.html
"""
from __future__ import absolute_import

# Stdlib imports
import os

# External packages imports
from celery import Celery

# Django and DRF imports
from django.conf import settings

# Set the default Django settings module for the 'celery' app.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings")

# you change change the name here
app = Celery("webservice")

# Celery-related configuration keys should have a `CELERY_` prefix.
app.config_from_object("django.conf:settings", namespace="CELERY")

# Load task modules from all registered Django app configs.
app.autodiscover_tasks(lambda: settings.INSTALLED_APPS)
