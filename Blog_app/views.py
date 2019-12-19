from django.shortcuts import render
from .models import *


# Create your views here.

# def baseview(request):


def indexview(request):
    random_blogs = BlogPost.objects.order_by('?')[:3]
    latest_blogs = BlogPost.objects.all().order_by('pub_date')

    return render(request, 'index.html', {
        'random_blogs': random_blogs,
        'latest_blogs': latest_blogs,
    })


def detail_blogview(request, pk):
    single_blog = BlogPost.objects.get(pk=pk)
    random_blogs = BlogPost.objects.order_by('?')[:3]

    return render(request, 'detail.html', {
        'single_blog': single_blog,
        'random_blogs': random_blogs
    })
