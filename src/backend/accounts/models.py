import secrets

from django.contrib.auth.models import AbstractUser
from django.db import models


class SubscriptionStatus(models.TextChoices):
    """Subscription status choices"""

    TRIAL = "trial", "Trial"
    ACTIVE = "active", "Active"
    EXPIRED = "expired", "Expired"
    CANCELED = "canceled", "Canceled"


class User(AbstractUser):
    """Custom user model for curated.guide"""

    # Stripe subscription
    stripe_customer_id = models.CharField(
        max_length=100, blank=True, help_text="Stripe customer ID"
    )
    subscription_status = models.CharField(
        max_length=20,
        choices=SubscriptionStatus.choices,
        default=SubscriptionStatus.TRIAL,
        help_text="Current subscription status",
    )
    trial_ends_at = models.DateTimeField(
        null=True, blank=True, help_text="When trial period ends"
    )

    class Meta:
        db_table = "users"
        verbose_name = "User"
        verbose_name_plural = "Users"

    def __str__(self):
        return self.username

    @property
    def invites_available(self):
        """Number of pending invitations available"""
        return self.sent_invitations.filter(status="pending").count()


class InvitationType(models.TextChoices):
    """Invitation type choices"""

    NORMAL = "normal", "Normal"  # Regular user invite
    FOUNDERS_PASS = "founders_pass", "Founder's Pass"  # Lifetime free


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
    invitation_type = models.CharField(
        max_length=20,
        choices=InvitationType.choices,
        default=InvitationType.NORMAL,
        help_text="Type of invitation",
    )
    stripe_coupon_id = models.CharField(
        max_length=100,
        blank=True,
        help_text="Stripe coupon ID (for Founder's Pass)",
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
