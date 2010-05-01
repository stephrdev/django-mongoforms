# -*- coding: utf-8 -*-

from mongoforms import MongoForm
from models import BlogPost

class BlogPostForm(MongoForm):
    class Meta:
        document = BlogPost
        fields = ('author', 'title', 'content', 'published')