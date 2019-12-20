from django.contrib.auth.models import AbstractUser
from django.db import models
from Custom_Admin.models import *


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)

    def __str__(self):
        return self.category_name


class BlogPost(models.Model):
    blog_title = models.CharField(max_length=100)
    blog_author = models.CharField(max_length=50)
    pub_date = models.DateTimeField(auto_now=True)
    blog_body = models.TextField()
    blog_image = models.ImageField()
    blog_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='userblog', blank=True)

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
    commented_date = models.DateTimeField(auto_now=True)
    blog_comment_id = models.IntegerField()

    def __str__(self):
        return self.user.username
