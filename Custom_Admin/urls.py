from django.urls import path
from .views import *

app_name = 'Custom_Admin'

urlpatterns = [
    path('', admin_indexview, name='admin_index'),
    path('Blog_app/category/add', add_category_view, name='add_category'),
    path('Blog_app/Blogpost/add', add_blog_view, name='add_blog'),
    path('Blog_app/category', category_list, name='category_list'),
    path('Blog_app/Blogpost', admin_blog_list, name='admin_blog_list'),
    path('Blog_app/Blogpost/<int:pk>/change', admin_blog_update, name='admin_blog_update'),
    path('Blog_app/category/<int:pk>/change', admin_category_update, name='admin_category_update'),

]
