from django.conf import settings
from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Invitation, User


@receiver(post_save, sender=User)
def create_user_invitations(sender, instance, created, **kwargs):
    """
    Create invitations for new users.

    When a user is created, automatically generate
    INVITATIONS_PER_USER invitation codes.
    """
    if created:
        invitations_count = getattr(
            settings, "INVITATIONS_PER_USER", 3
        )
        for _ in range(invitations_count):
            Invitation.objects.create(sender=instance)
