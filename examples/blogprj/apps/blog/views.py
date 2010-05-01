# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponseRedirect

from models import BlogPost
from forms import BlogPostForm

def index(request, slug=None, template_name='blog/index.html'):
    posts = BlogPost.objects[:5]
    template_context = {'posts': posts}
    #print posts[0].get_absolute_url()
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )

def show(request, slug, template_name='blog/show.html'):
    post = BlogPost.objects.get(slug=slug)
    template_context = {'post': post}
    
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )

def new(request, template_name='blog/new_or_edit.html'):
    if request.method == 'POST':
        form = BlogPostForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect("/")
    else:
        form = BlogPostForm()
    
    template_context = {'form': form}
    
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )

def delete(request, slug):
    post = BlogPost.objects(slug=slug)
    post.delete()
    return HttpResponseRedirect("/")

def edit(request, slug, template_name='blog/new_or_edit.html'):
    
    post = BlogPost.objects.get(slug=slug)
    if request.method == 'POST':
        form = BlogPostForm(request.POST, instance=post)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect(post.get_absolute_url())
    else:
        form = BlogPostForm(instance=post)
    
    template_context = {'form': form}
    
    return render_to_response(
        template_name,
        template_context,
        RequestContext(request)
    )