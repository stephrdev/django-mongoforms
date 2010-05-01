# -*- coding: utf-8 -*-

from django import forms
from mongoforms import MongoForm
from models import BlogPost

class BlogPostForm(MongoForm):
    class Meta:
        document = BlogPost
        fields = ('author', 'title', 'content', 'published')
    content = forms.CharField(widget=forms.Textarea)