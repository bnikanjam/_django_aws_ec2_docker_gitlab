#!/usr/bin/env python

# Stdlib imports
import os
import sys

# External packages imports
import environ

env = environ.Env()
environ.Env.read_env()  # Read .env

APP_ENV = env("APP_ENV")
if APP_ENV is None:
    raise RuntimeError("APP_ENV environment variable not found.")


def main():
    """Run administrative tasks."""

    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "webservice.settings.development")
    try:
        # Django and DRF
        # Core Django and DRF imports
        # Django and DRF imports
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc

    # Disable certain manage.py commands in production.
    DISABLED_COMMANDS = ["RESET_DB", "FLUSH", "LOADDATA"]
    if len(sys.argv) > 1 and APP_ENV == "PRODUCTION" and sys.argv[1] in DISABLED_COMMANDS:
        error_msg = "{} disabled in production.".format(" ".join(sys.argv))
        raise RuntimeError(error_msg)

    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
