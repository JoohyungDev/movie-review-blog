from django.db import models
from pathlib import Path
from django.contrib.auth.models import User


class Category(models.Model):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=200, unique=True, allow_unicode=True)

    def __str__(self):
        return self.name

    def post_count(self):
        return self.post_set.count()

    class Meta:
        verbose_name_plural = "Categories"


class Post(models.Model):
    title = models.CharField(max_length=30)
    hook_text = models.CharField(max_length=100, blank=True)
    content = models.TextField()

    thumbnail_image = models.ImageField(upload_to="blog/images/%Y/%m/%d/", blank=True)
    file_upload = models.FileField(upload_to="blog/files/%Y/%m/%d", blank=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    author = models.ForeignKey(User, on_delete=models.CASCADE)

    category = models.ForeignKey(
        Category, null=True, blank=True, on_delete=models.SET_NULL
    )

    def __str__(self):
        return f"{self.title}"

    def get_absolute_url(self):
        return f"/blog/{self.pk}/"

    def get_file_name(self):
        return self.file_upload.name

    def get_file_ext(self):
        return Path(self.get_file_name()).suffix[1:]
