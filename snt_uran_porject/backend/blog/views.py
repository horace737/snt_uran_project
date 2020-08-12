#! /usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import unicode_literals

from django.shortcuts import render, get_object_or_404
from .models import *


def posts_list(request):
    posts = Post.objects.filter(active=True)
    context = {
        'posts': posts
    }
    return render(request, 'blog/posts-list.html', context=context)


def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)

    if post:
        post.view += 1
        post.save()

    context = {
        'post': post,
    }
    return render(request, 'blog/post-detail.html', context=context)
