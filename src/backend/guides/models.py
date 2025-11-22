from django.conf import settings
from django.db import models
from django.utils.text import slugify


class Guide(models.Model):
    """A curated guide created by a user"""

    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='guides'
    )
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200)
    description = models.TextField(blank=True)
    cover_image = models.ImageField(upload_to='guide_covers/', blank=True, null=True)

    # Privacy
    is_public = models.BooleanField(default=True)
    password = models.CharField(max_length=128, blank=True)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'guides'
        ordering = ['-created_at']
        unique_together = [('owner', 'slug')]

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)


class Item(models.Model):
    """An item within a guide"""

    guide = models.ForeignKey(
        Guide,
        on_delete=models.CASCADE,
        related_name='items'
    )
    title = models.CharField(max_length=300)
    note = models.TextField(blank=True, help_text="Why you love this")
    image = models.ImageField(upload_to='item_images/', blank=True, null=True)

    # Links (simple JSON field for now, can be normalized later)
    links = models.JSONField(default=list, blank=True)

    # Ordering
    position = models.PositiveIntegerField(default=0)

    # Timestamps
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        db_table = 'items'
        ordering = ['position', 'created_at']

    def __str__(self):
        return f"{self.guide.title} - {self.title}"
