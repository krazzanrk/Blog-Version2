# Generated by Django 3.0 on 2019-12-17 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blog_app', '0003_auto_20191217_0646'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='author',
            new_name='blog_author',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='body',
            new_name='blog_body',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='category',
            new_name='blog_category',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='image',
            new_name='blog_image',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='title',
            new_name='blog_title',
        ),
    ]
