from django.contrib import admin

from .models import *

class CollectionAdmin(admin.ModelAdmin):
    list_display = ('collection_id', 'title_en', 'date_created', 'date_updated', 'presentation_order')
    sortable_by = ('presentation_order',)
    ordering = ('presentation_order',)

class OnlineResourceCategoryAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'description_en', 'presentation_order')
    sortable_by = ('presentation_order',)
    ordering = ('presentation_order',)

class OnlineResourceAdmin(admin.ModelAdmin):
    list_display = ('category_id', 'title', 'description_en', 'description_vi', 'url', 'date_created', 'date_updated')
    sortable_by = ('category_id',)
    ordering = ('category_id',)

    # Register your models here.
admin.site.register(Collection, CollectionAdmin)
admin.site.register(Document)
admin.site.register(BlogType)
admin.site.register(Blog)
admin.site.register(OCR)
admin.site.register(OnlineResourceCategory, OnlineResourceCategoryAdmin)
admin.site.register(OnlineResource, OnlineResourceAdmin)