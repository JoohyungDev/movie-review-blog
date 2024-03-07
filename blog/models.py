from django.db import models
from pathlib import Path


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=30)
    content = models.TextField()

    thumbnail_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"

    def get_file_name(self):
        return self.file_upload.name

    def get_file_ext(self):
        return Path(self.get_file_name()).suffix[1:]
