# Stdlib imports
import uuid as uuid_lib

# Django and DRF imports
from django.db import models
from django.utils import timezone


class TimeStampMixin(models.Model):
    """
    Add timestamp fields for when a model instance first created and last modified.
    """

    created_at = models.DateTimeField(default=timezone.now, editable=False, blank=True)
    updated_at = models.DateTimeField(editable=True, blank=True)

    class Meta:
        abstract = True

    # Ensure created_at == updated_at when 1st created.
    def save(self, *args, **kwargs):
        self.updated_at = self.created_at if self.id is None else timezone.now()
        super().save(*args, **kwargs)


class BaseModel(TimeStampMixin, models.Model):
    """
    Base model class with both
        id:     Django's default sequential integers as pk for best database query "Performance".
        uuid:   Non-Sequential keys as lookup fields at external API endpoints for "Security".
    and
        created_at and updated_at fields
    and
        Enforcing data validations prior to saving.
    """

    id = models.AutoField(primary_key=True)
    uuid = models.UUIDField(default=uuid_lib.uuid4, editable=False, unique=True, db_index=True)

    # Enforce data validations prior to saving. Additional validation checks
    # should be performed by overriding the clean() method at sub model classes.
    def save(self, *args, **kwargs):
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True
