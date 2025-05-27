from django import forms
from .models import Author, Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "title body author image".split(" ")