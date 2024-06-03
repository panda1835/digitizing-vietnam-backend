from django.contrib import admin

from .models import *

class OnlineResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_name', 'description', 'presentation_order')
    sortable_by = ('presentation_order',)
    ordering = ('presentation_order',)

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collection_id', 'title', 'date_created', 'date_updated', 'presentation_order')
    sortable_by = ('presentation_order',)
    ordering = ('presentation_order',)

    # Register your models here.
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Document)
admin.site.register(BlogType)
admin.site.register(Blog)
admin.site.register(OCR)
admin.site.register(OnlineResourceCategory, OnlineResourceCategoryAdmin)
admin.site.register(OnlineResource)