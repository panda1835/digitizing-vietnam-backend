from django.db import models
from django.utils import timezone


class Collection(models.Model):
    collection_id = models.CharField(max_length=255, primary_key=True)
    title_en = models.CharField(max_length=255, blank=False)
    title_vi = models.CharField(max_length=255, blank=True)
    description_en = models.TextField(blank=False)
    description_vi = models.TextField(blank=True)
    image_url = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    presentation_order = models.IntegerField(default=1000)

    def __str__(self):
        return f"{self.title_en}"

    def formatted_date_created(self):
        return self.date_created.strftime('%B %d, %Y')

    def formatted_date_updated(self):
        return self.date_updated.strftime('%B %d, %Y')


class Document(models.Model):
    document_id = models.CharField(max_length=255, primary_key=True)
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE)
    title_en = models.CharField(max_length=255, blank=False)
    title_vi = models.CharField(max_length=255, blank=True)
    description_en = models.TextField(blank=True)
    description_vi = models.TextField(blank=True)
    image_url = models.CharField(max_length=255, blank=False)
    manifest = models.TextField(blank=False, default="{}")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    presentation_order = models.IntegerField(default=1000)

    def __str__(self):
        return f"({self.collection_id.title_en}) {self.title_en}"

    def formatted_date_created(self):
        return self.date_created.strftime('%B %d, %Y')

    def formatted_date_updated(self):
        return self.date_updated.strftime('%B %d, %Y')


class BlogType(models.Model):
    blog_type = models.CharField(max_length=50, primary_key=True)

    def __str__(self):
        return self.blog_type


class Blog(models.Model):
    blog_id = models.CharField(max_length=255, primary_key=True)
    blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
    related_collection = models.ManyToManyField(Collection, blank=True, related_name="blogs")
    title = models.CharField(max_length=255, blank=False)
    author = models.CharField(max_length=255, default="Admin", blank=False)
    content = models.TextField(blank=False)
    image_url = models.CharField(max_length=255, blank=False, default="https://via.placeholder.com/500")
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"({self.blog_type}) {self.title} (by {self.author})"

    def formatted_date_created(self):
        return self.date_created.strftime('%B %d, %Y')

    def formatted_date_updated(self):
        return self.date_updated.strftime('%B %d, %Y')


class OCR(models.Model):
    collection_id = models.ForeignKey(Collection, on_delete=models.CASCADE, default=None)
    document_id = models.ForeignKey(Document, on_delete=models.CASCADE)
    canvas_id = models.CharField(max_length=255)
    text = models.TextField(blank=True)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"OCR for {self.document_id.title_en} (canvas {self.canvas_id})"

    def formatted_date_created(self):
        return self.date_created.strftime('%B %d, %Y')

    def formatted_date_updated(self):
        return self.date_updated.strftime('%B %d, %Y')

class OnlineResourceCategory(models.Model):
    category_id = models.CharField(max_length=255, primary_key=True, blank=False)
    category_name_en = models.CharField(max_length=255, blank=True)
    category_name_vi = models.CharField(max_length=255, blank=True)
    description_en = models.TextField(blank=False)
    description_vi = models.TextField(blank=True)
    image_url = models.TextField(blank=False, default="https://via.placeholder.com/500")
    presentation_order = models.IntegerField(default=1000)

    def __str__(self):
        return self.category_id

class OnlineResource(models.Model):
    category_id = models.ForeignKey(OnlineResourceCategory, on_delete=models.CASCADE)
    title = models.CharField(max_length=255, primary_key=True)
    description_en = models.TextField(blank=False)
    description_vi = models.TextField(blank=True)
    url = models.CharField(max_length=255, blank=False)
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} - {self.url}"

    def formatted_date_created(self):
        return self.date_created.strftime('%B %d, %Y')

    def formatted_date_updated(self):
        return self.date_updated.strftime('%B %d, %Y')