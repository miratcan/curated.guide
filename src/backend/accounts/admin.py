from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from .models import Invitation, User


@admin.register(User)
class UserAdmin(BaseUserAdmin):
    """Admin for custom User model"""

    list_display = BaseUserAdmin.list_display + ("invites_available",)
    fieldsets = BaseUserAdmin.fieldsets + (
        ("Invite System", {"fields": ("invites_available",)}),
    )


@admin.register(Invitation)
class InvitationAdmin(admin.ModelAdmin):
    list_display = (
        "code",
        "sender",
        "recipient_email",
        "status",
        "used_by",
        "created_at",
    )
    list_filter = ("status", "created_at")
    search_fields = (
        "code",
        "sender__username",
        "recipient_email",
        "used_by__username",
    )
    readonly_fields = ("code", "created_at", "used_at")
