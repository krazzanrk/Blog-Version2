from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect, get_object_or_404
from .forms import *
from Blog_app.models import *


# Create your views here.
def admin_indexview(request):
    return render(request, 'custom_admin/main_admin.html')


def add_category_view(request):
    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            Category.objects.create(**form.cleaned_data)
            return redirect('Custom_Admin:category_list')
    else:
        form = CategoryForm()
    context = {'my_form': form}
    return render(request, 'custom_admin/add_category.html', context)


def category_list(request):
    categories = Category.objects.all()

    return render(request, 'custom_admin/category_list.html', {'categories': categories})


def add_blog_view(request):
    if request.method == 'POST':
        form = BlogAddForm(request.POST, request.FILES)
        if form.is_valid():
            BlogPost.objects.create(**form.cleaned_data)
            return redirect('Custom_Admin:admin_blog_list')

    else:
        form = BlogAddForm()

    return render(request, 'custom_admin/Add_blog.html', {'form': form})


def admin_blog_list(request):
    blog_list = BlogPost.objects.all()
    return render(request, 'custom_admin/admin_blogpost_list.html', {'bloglists': blog_list})


def admin_blog_update(request, pk):
    blog_instance = get_object_or_404(BlogPost, pk=pk)

    if request.method == 'POST':
        form = BlogAddForm(request.POST, request.FILES)
        if form.is_valid():
            blog_instance.blog_title = form.cleaned_data['blog_title']
            blog_instance.blog_author = form.cleaned_data['blog_author']
            blog_instance.pub_date = form.cleaned_data['pub_date']
            blog_instance.blog_body = form.cleaned_data['blog_body']
            blog_instance.blog_image = form.cleaned_data['blog_image']
            blog_instance.blog_category = form.cleaned_data['blog_category']
            blog_instance.save()
            return redirect('Custom_Admin:admin_blog_list')

    else:
        form = BlogAddForm()

    return render(request, 'custom_admin/blog_update.html', {'update_blog': blog_instance, 'form': form})


def admin_category_update(request, pk):
    category_instance = get_object_or_404(Category, pk=pk)
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        print(form)

        if form.is_valid():
            category_instance.category_name = form.cleaned_data['category_name']
            category_instance.save()
            # return redirect('Custom_Admin:category_list')

    else:
        form = CategoryForm()

    return render(request, 'custom_admin/category_update.html',
                  {'form': form, 'update_category': category_instance})


def delete_confirmview(request,pk):

    cat_instant=get_object_or_404(Category,pk=pk)

    if request.method == 'POST':
        form = ConfirmForm(request.POST)

        if form.is_valid():

            item_id = request.POST.get('item_id')
            category=Category.objects.get(pk=item_id)
            category.delete()

            return redirect('Custom_Admin:category_list')

    else:
        form = ConfirmForm()


    return render(request, 'custom_admin/confirm_delete.html',
              {
                  'form': form,
               'cat_instant':cat_instant})



def registration_view(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            print("Form Validate")
            username = form.cleaned_data['username']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            first_name = form.cleaned_data['first_name']
            middle_name = form.cleaned_data['middle_name']
            last_name = form.cleaned_data['last_name']

            User.objects.create_user(username, email, password, first_name=first_name, middle_name=middle_name,
                                     last_name=last_name)

            return redirect('Custom_Admin:login')

    else:
        form = RegistrationForm()

    return render(request, 'custom_admin/registrations/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('Custom_Admin:admin_index')

            else:
                return redirect('Custom_Admin:add_blog')

    else:
        form = LoginForm()

    return render(request, 'custom_admin/registrations/register.html', {'form': form})


def logout_view(request):
    logout(request)
    return redirect('Custom_Admin:register')
