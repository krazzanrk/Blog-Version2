from django.urls import path
from .views import *

app_name = 'Blog_app'

urlpatterns = [

    path('', indexview, name='index'),
    path('detail/<int:pk>', detail_blogview, name='detail_blog'),
    path('category/', category_listview, name='blog_category_list'),
    path('category/<int:pk>', blogtiltle_by_category_view, name='blogtitle_category_list'),
]
