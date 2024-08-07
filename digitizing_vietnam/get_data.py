import json
import os
import glob

from .models import *

def get_blogs_by_type(blog_type):
    if (blog_type not in ["news", "highlights", "initiatives"]):
        return {"error": "Invalid blog type."}

    blogs = Blog.objects.filter(blog_type=blog_type.capitalize())
    blogs_data = []
    for blog in blogs:
        blogs_data.append({
            "blog_id": blog.blog_id,
            "title": blog.title,
            "author": blog.author,
            "image_url": blog.image_url,
            "date_created": blog.formatted_date_created(),
        })
    return {"data": blogs_data}

def get_blog_post_by_id(blog_id):
    blog = Blog.objects.get(blog_id=blog_id)
    if blog:
        return {"data": {
            "title": blog.title,
            "author": blog.author,
            "content": blog.content,
            "image_url": blog.image_url,
            "date_created": blog.formatted_date_created(),
        }}
    else:
        return {"error": "Blog post not found."}
    
def get_blog_post_by_related_collection(collection_id):
    blogs = Blog.objects.filter(related_collection=collection_id)
    if not Collection.objects.filter(collection_id=collection_id).exists():
        return {"error": "Invalid collection ID."}
    blogs_data = []
    for blog in blogs:
        blogs_data.append({
            "blog_id": blog.blog_id,
            "title": blog.title,
            "image_url": blog.image_url,
        })
    return {"data": blogs_data}

def get_documents_of_collection(collection_id, lang):
    try:
        collection = Collection.objects.get(collection_id=collection_id)
        # Get all documents in the collection
        documents = Document.objects.filter(collection_id=collection_id).order_by('document_id')

        return {"data": {
            "title": collection.title_en if lang == "en" else collection.title_vi,
            "description": collection.description_en if lang == "en" else collection.description_vi,
            "image_url": collection.image_url,
            "documents": [
                {
                    "document_id": document.document_id,
                    "title": document.title_en if lang == "en" else document.title_vi,
                    "image_url": document.image_url,
                } for document in documents
            ]
        }}
    except:
        return {"error": "Invalid collection ID."}

    return {"error": "Invalid collection ID."}

def get_all_collections(lang):
    all_collections = Collection.objects.all().order_by('presentation_order')
    collections_data = []
    for collection in all_collections:
        collections_data.append({
            "collection_id": collection.collection_id,
            "title": collection.title_en if lang == "en" else collection.title_vi,
            "description": collection.description_en if lang == "en" else collection.description_vi,
            "image_url": collection.image_url,
        })
    
    return {"data": collections_data}

def get_ocr(collection_id, document_id, canvas_id):
    if (Collection.objects.filter(collection_id=collection_id).count() == 0):
        return {"error": "Invalid collection ID."}
    if (Document.objects.filter(document_id=document_id).count() == 0):
        return {"error": "Invalid document ID."}
    if (OCR.objects.filter(collection_id=collection_id, document_id=document_id, canvas_id=canvas_id).count() == 0):
        return {"text": "No OCR text for this page."}
    
    data = OCR.objects.get(collection_id=collection_id, document_id=document_id, canvas_id=canvas_id)
    return {"text": data.text}
    

def get_manifest(collection_id, document_id):
    try:
        data = Document.objects.get(collection_id=collection_id, document_id=document_id)
        return eval(data.manifest)
    except Exception as e:
        return {"error": "Invalid document ID or canvas ID."}

def get_online_resources(lang):
    resource_categories = OnlineResourceCategory.objects.all().order_by('presentation_order')
    online_resources = OnlineResource.objects.all()
    
    resources_data = []

    for category in resource_categories:
        resources_data.append({
            "category_name": category.category_name_en if lang == "en" else category.category_name_vi,
            "description": category.description_en if lang == "en" else category.description_vi,
            "image_url": category.image_url,
            "resources": [
                {
                    "title": resource.title,
                    "description": resource.description_en if lang == "en" else resource.description_vi,
                    "url": resource.url,
                } for resource in online_resources if resource.category_id == category
            ]
        })
    
    return {"data": resources_data}