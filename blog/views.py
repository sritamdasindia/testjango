# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from .models import *
import datetime
from .forms import BlogEntryForm
# Create your views here.
def index(request):
    return render(request,'blog/index.html')

def posts(request):
    if request.method=="POST":
        form = BlogEntryForm(request.POST)
        # post_text = request.POST["post"]
        # post_ = BlogEntry(text = post_text,timestamp=datetime.datetime.now())
        # post_.save(force_insert=True)
        if form.is_valid():
            post = form.save(commit=False)
            post.text = request.POST["text"]
            post.timestamp = datetime.datetime.now()
            post.save()
        return render(request,'blog/posts.html')
    elif request.method == "GET":
        form = BlogEntryForm()
        return render(request,'blog/posts.html',{"form":form})

def show( request):

    obj = BlogEntry.objects.all()

    return render( request, 'blog/success.html', context = {'data' : obj })
