from django.contrib import admin

from .models import Collection, Document, Blog, OCR, BlogType
# Register your models here.
admin.site.register(Collection)
admin.site.register(Document)
admin.site.register(BlogType)
admin.site.register(Blog)
admin.site.register(OCR)