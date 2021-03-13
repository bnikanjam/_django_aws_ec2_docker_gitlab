# Django and DRF imports
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

# This app/directory imports
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    # Removed the username field.
    username = None
    # Make the email field required and unique.
    email = models.EmailField(_("email address"), unique=True)

    # Set the USERNAME_FIELD which defines the unique identifier for
    # the User model to email.
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    # All objects for the class come from the CustomUserManager.
    objects = CustomUserManager()

    def __str__(self):
        return self.email
