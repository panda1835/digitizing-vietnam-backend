from django.urls import path

from . import views

urlpatterns = [
    path('status', views.status, name='status'),
    path('manifest/<str:collection_id>/<str:document_id>', views.manifest, name='manifest'),
    path('ocr/<str:collection_id>/<str:document_id>', views.ocr, name='ocr'),
    path('collections', views.all_collections, name='collections'),
    path('collections/<str:collection_id>', views.documents_of_collection, name='documents_of_collection'),
    path('blogs/<str:blog_type>', views.blogs_by_type, name='blogs_by_type'),
    path('blogs', views.blog_post, name='blog_post'),
    path('online-resources', views.online_resources, name='online_resources'),
]