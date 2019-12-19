from django import forms
from Blog_app.models import *
from .models import *


class CategoryForm(forms.Form):
    category_name = forms.CharField(max_length=50, min_length=5)

    def clean_category_name(self):
        category_name = self.cleaned_data.get('category_name')
        category_name_exist = Category.objects.filter(category_name__iexact=category_name).count()

        if category_name_exist > 0:
            raise forms.ValidationError('This title has already been used. Please try again.')

        return category_name


class BlogAddForm(forms.Form):
    blog_title = forms.CharField(max_length=100, min_length=5)
    blog_author = forms.CharField(max_length=50, min_length=3)
    pub_date = forms.DateField()
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


class ConfirmForm(forms.Form):
    item_id = forms.IntegerField()


class CategoryDeleteForm(forms.Form):
    cat_id = forms.IntegerField()


class RegistrationForm(forms.Form):
    first_name = forms.CharField(widget=forms.TextInput())
    middle_name = forms.CharField(widget=forms.TextInput())
    last_name = forms.CharField(widget=forms.TextInput())
    username = forms.CharField(widget=forms.TextInput())

    email = forms.CharField(widget=forms.EmailInput())
    password = forms.CharField(widget=forms.PasswordInput())
    confirm_password = forms.CharField(widget=forms.PasswordInput())

    def clean_confirm_password(self):
        password = self.cleaned_data['password']
        confirm_password = self.cleaned_data['confirm_password']
        if password != confirm_password:
            raise forms.ValidationError("Entered password and confirm password not match. Enter password again")
        return confirm_password

    def clean_username(self):
        username = self.cleaned_data.get('username')
        username_exist = BlogPost.objects.filter(user__username__iexact=username).count()

        if username_exist > 0:
            raise forms.ValidationError('This title has already been used. Please try again.')

        return username


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput())
    password = forms.CharField(widget=forms.PasswordInput())
