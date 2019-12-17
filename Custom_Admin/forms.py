from django import forms
from Blog_app.models import *


class CategoryForm(forms.Form):
    category_name = forms.CharField(max_length=50, min_length=5)

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        category_name_exist = Category.objects.filter(category_name__iexact=category_name).count()

        if category_name_exist > 0:
            raise forms.ValidationError('This title has already been used. Please try again.')

        return category_name


class BlogAddForm(forms.Form):
    blog_title = forms.CharField(max_length=100,min_length=5)
    blog_author = forms.CharField(max_length=50,min_length=3)
    pub_date = forms.DateTimeField()
    blog_body = forms.CharField(widget=forms.Textarea)
    blog_image = forms.ImageField()
    blog_category = forms.ModelChoiceField(queryset=Category.objects.all())

    def clean_blog_title(self):
        blog_title = self.cleaned_data.get('blog_title')
        blog_name_exist = BlogPost.objects.filter(blog_title__iexact=blog_title).count()

        if blog_name_exist > 0:
            raise forms.ValidationError('This title has already been used. Please try again.')

        return blog_title


class DeleteForm(forms.Form):
    item_id = forms.IntegerField()


class CategoryDeleteForm(forms.Form):
    cat_id = forms.IntegerField()
