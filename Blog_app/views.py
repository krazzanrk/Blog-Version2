from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, redirect
from .models import *
from .forms import *


# Create your views here.

# def baseview(request):


def indexview(request):
    blog = BlogPost.objects.all().order_by('-pub_date')
    random_blogs = BlogPost.objects.order_by('?')[:3]
    latest_blogs = BlogPost.objects.all().order_by('pub_date')

    paginator = Paginator(blog, 2)
    page = request.GET.get('page', 1)
    try:
        blog_page = paginator.page(page)
    except PageNotAnInteger:
        blog_page = paginator.page(1)
    except EmptyPage:
        blog_page = paginator.page(paginator.num_pages)

    return render(request, 'index.html', {
        'random_blogs': random_blogs,
        'latest_blogs': latest_blogs,
        'blog_pages': blog_page
    })


def detail_blogview(request, pk):
    single_blog = BlogPost.objects.get(pk=pk)
    random_blogs = BlogPost.objects.order_by('?')[:3]
    comments = Comment.objects.all()

    if request.method == "POST":
        form = CommentForm(request.POST)

        if form.is_valid():
            Comment.objects.create(**form.cleaned_data, user_id=request.user.id)

        else:
            print(form.errors)
    else:
        form = CommentForm()

    return render(request, 'detail.html', {
        'single_blog': single_blog,
        'random_blogs': random_blogs,
        'form': form,
        'comments': comments

    })


def category_listview(request):
    category = Category.objects.all()

    return render(request, 'blog_by_categories.html', {'categories': category})


def blogtiltle_by_category_view(request, pk):

    blog_title_by_category = BlogPost.objects.filter(blog_category_id=pk)
    category_name=BlogPost.objects.filter(blog_category_id=pk).first()
    blog_number=BlogPost.objects.filter(blog_category_id=pk).count()

    return render(request, 'blog_tile_by_categories.html', {'blog_titles': blog_title_by_category,
                                                            'blog_no':blog_number,
                                                           'cat_name':category_name })
