from django.db import models


class TimeStampedModel(models.Model):
    """
    Abstract base model with timestamp and soft delete fields.

    Inherit from this model to add:
    - created_at
    - updated_at
    - is_deleted
    - deleted_at
    """

    created_at = models.DateTimeField(
        auto_now_add=True, help_text="When this record was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="When this record was last updated"
    )

    # Soft delete
    is_deleted = models.BooleanField(
        default=False, help_text="Whether this record is soft-deleted"
    )
    deleted_at = models.DateTimeField(
        null=True, blank=True, help_text="When this record was deleted"
    )

    class Meta:
        abstract = True
