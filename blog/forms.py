from .models import Comment, Profile
from django import forms
from django.contrib.auth.models import User


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["first_name", "last_name"]


class ProfileForm(forms.ModelForm):
    profile_photo = forms.ImageField(required=False)

    class Meta:
        model = Profile
        fields = ["nickname", "profile_photo"]
