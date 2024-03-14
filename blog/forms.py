from .models import Comment, ReComment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ("content",)


class ReCommentForm(forms.ModelForm):
    class Meta:
        model = ReComment
        fields = ("content",)
