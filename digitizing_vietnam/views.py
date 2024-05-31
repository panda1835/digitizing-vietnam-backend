from django.http import JsonResponse, HttpResponse
import json
import os
import time

from .models import Collection, Document, Blog, OCR

from . import get_data

def status(request):
    return JsonResponse({"status": "OK"})

def manifest(request, collection_id, document_id):
    data = get_data.get_manifest(collection_id, document_id)
    return JsonResponse(data)

def collections(request):
    data = get_data.get_collection()
    return JsonResponse(data)

def collection_by_id(request, collection_id):
    data = get_data.get_collection_by_id(collection_id)
    return JsonResponse(data)

def blog_post(request):
    # Access the query parameters
    query_params = request.GET

    blog_id = query_params.get('blog-id', None)  # Returns None if 'blog-id' is not present in the query parameters
    related_collection = query_params.get('related-collection', None)

    if blog_id:
        data = get_data.get_blog_post_by_id(blog_id)

    if related_collection:
        data = get_data.get_blog_post_by_related_collection(related_collection)

    return JsonResponse(data)

def blogs_by_type(request, blog_type):
    data = get_data.get_blogs_by_type(blog_type)
    return JsonResponse(data)

def ocr(request, collection_id, document_id):
    canvas_id = request.GET.get('canvasId', "")
    data = get_data.get_ocr(collection_id, document_id, canvas_id)
    return JsonResponse(data)