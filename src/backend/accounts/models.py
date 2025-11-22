import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Custom user model for curated.guide"""

    # Invite system
    invites_available = models.PositiveIntegerField(
        default=3, help_text="Number of invites available"
    )

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username


class Invitation(models.Model):
    """Invitation code for invite-only access"""

    STATUS_CHOICES = [
        ("pending", "Pending"),
        ("accepted", "Accepted"),
        ("expired", "Expired"),
    ]

    code = models.CharField(
        max_length=32,
        unique=True,
        help_text="Unique invitation code",
    )
    sender = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="sent_invitations",
        help_text="User who created this invitation",
    )
    recipient_email = models.EmailField(
        blank=True,
        help_text="Email of invited person (optional)",
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default="pending",
        help_text="Status of invitation",
    )

    # Usage tracking
    used_by = models.OneToOneField(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name="used_invitation",
        help_text="User who accepted this invitation",
    )
    used_at = models.DateTimeField(
        null=True,
        blank=True,
        help_text="When this invitation was used",
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True,
        help_text="When this invitation was created",
    )

    class Meta:
        db_table = "invitations"
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.code} ({self.status})"

    def save(self, *args, **kwargs):
        if not self.code:
            self.code = secrets.token_urlsafe(16)
        super().save(*args, **kwargs)
