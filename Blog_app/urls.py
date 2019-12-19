from django.urls import path
from .views import *


app_name='Blog_app'


urlpatterns=[

    path('',indexview,name='index'),
    path('detail/<int:pk>',detail_blogview,name='detail_blog')
]