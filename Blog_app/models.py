from django.db import models


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

    def __str__(self):
        return self.blog_title


class Comment(models.Model):
    username = models.CharField(max_length=200)
    message = models.TextField()
    commented_date = models.DateTimeField(auto_now=True)
    blog_comment_id = models.IntegerField()

    def __str__(self):
        return self.username
