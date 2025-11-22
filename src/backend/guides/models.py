from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Guide(models.Model):
    """A curated guide created by a user"""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="guides",
        help_text="User who created this guide",
    )
    title = models.CharField(max_length=200, help_text="Title of the guide")
    slug = models.SlugField(
        max_length=200, help_text="URL-friendly version of title"
    )
    description = models.TextField(
        blank=True, help_text="Description of what this guide is about"
    )
    cover_image = models.ImageField(
        upload_to="guide_covers/",
        blank=True,
        null=True,
        help_text="Cover image for the guide",
    )

    # Privacy & Visibility
    is_public = models.BooleanField(
        default=True, help_text="Whether this guide is publicly accessible"
    )
    is_listed = models.BooleanField(
        default=True, help_text="Whether this guide appears on user's profile"
    )
    password = models.CharField(
        max_length=128,
        blank=True,
        help_text="Password for password-protected guides",
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="When this guide was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="When this guide was last updated"
    )

    # Soft delete
    is_deleted = models.BooleanField(
        default=False, help_text="Whether this guide is soft-deleted"
    )
    deleted_at = models.DateTimeField(
        null=True, blank=True, help_text="When this guide was deleted"
    )

    class Meta:
        db_table = "guides"
        ordering = ["-created_at"]
        unique_together = [("owner", "slug")]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Link(models.Model):
    """A link associated with an item"""

    url = models.URLField(max_length=500, help_text="URL of the link")
    label = models.CharField(
        max_length=200, blank=True, help_text="Display label for the link"
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="When this link was created"
    )

    class Meta:
        db_table = "links"

    def __str__(self):
        return self.label or self.url


class Item(models.Model):
    """An item within a guide"""

    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        related_name="items",
        help_text="Guide this item belongs to",
    )
    title = models.CharField(max_length=300, help_text="Title of the item")
    note = models.TextField(blank=True, help_text="Why you love this item")
    image = models.ImageField(
        upload_to="item_images/",
        blank=True,
        null=True,
        help_text="Image for this item",
    )

    # Links
    links = models.ManyToManyField(
        Link,
        blank=True,
        related_name="items",
        help_text="Links associated with this item",
    )

    # Ordering
    position = models.PositiveIntegerField(
        default=0, help_text="Position of this item in the guide"
    )

    # Timestamps
    created_at = models.DateTimeField(
        auto_now_add=True, help_text="When this item was created"
    )
    updated_at = models.DateTimeField(
        auto_now=True, help_text="When this item was last updated"
    )

    class Meta:
        db_table = "items"
        ordering = ["position", "created_at"]

    def __str__(self):
        return f"{self.guide.title} - {self.title}"
