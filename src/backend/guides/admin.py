from django.contrib import admin

from .models import Guide, Item, Link


class ItemInline(admin.TabularInline):
    model = Item
    extra = 1
    fields = ("title", "note", "position")


@admin.register(Guide)
class GuideAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "is_public", "created_at")
    list_filter = ("is_public", "created_at")
    search_fields = ("title", "description", "owner__username")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ItemInline]


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ("title", "guide", "position", "created_at")
    list_filter = ("created_at",)
    search_fields = ("title", "note", "guide__title")
    filter_horizontal = ("links",)


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("url", "label", "created_at")
    search_fields = ("url", "label")
