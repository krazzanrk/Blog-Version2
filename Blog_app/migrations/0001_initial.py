# Generated by Django 3.0 on 2019-12-19 07:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=200)),
                ('message', models.TextField()),
                ('commented_date', models.DateTimeField(auto_now=True)),
                ('blog_comment_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='BlogPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('blog_title', models.CharField(max_length=100)),
                ('blog_author', models.CharField(max_length=50)),
                ('pub_date', models.DateTimeField(auto_now=True)),
                ('blog_body', models.TextField()),
                ('blog_image', models.ImageField(upload_to='')),
                ('blog_category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Blog_app.Category')),
            ],
        ),
    ]
