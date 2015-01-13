# -*- coding: utf-8 -*-
from django.shortcuts import render, get_object_or_404, render_to_response
from django.http import HttpResponse
from article.models import Article
from datetime import datetime

# Create your views here.
def home(request):
    post_list = Article.objects.all()
    return render(request, 'home.html', {'post_list': post_list})

def detail(request, id):
    post = get_object_or_404(Article, id = int(id))
    return render(request, 'post.html', {'post': post})

def archives(request):
    post_list = Article.objects.all()
    return render(request, 'archives.html', {'post_list': post_list, 'error' : False})

def search_tag(request, tag) :
    try:
        post_list = Article.objects.filter(category__iexact = tag) #contains
    except Article.DoesNotExist :
        raise Http404
    return render(request, 'tag.html', {'post_list' : post_list})

def about_me(request):
    return render(request, 'aboutme.html')

def blog_search(request):
    if 's' in request.GET:
        s = request.GET['s']
        if s:
            post_list = Article.objects.filter(title__icontains = s)
            if len(post_list) == 0 :
                return render(request,'archives.html', {'post_list' : post_list, 'error' : True})
            else :
                return render(request,'archives.html', {'post_list' : post_list, 'error' : False})
    return redirect('/')
