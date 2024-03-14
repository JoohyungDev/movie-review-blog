from django.db import models
from django.contrib.auth.models import User
from sorl.thumbnail import ImageField


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nickname = models.CharField(max_length=64)
    profile_photo = models.ImageField(blank=True)


class Photo(models.Model):
    image = models.ImageField(upload_to="accounts/images/thumbnail/%Y/%m/%d/")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return "{} {} {}".format(self.user.username, self.content, self.is_public)
