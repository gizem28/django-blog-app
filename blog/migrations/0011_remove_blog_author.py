# Generated by Django 4.0.2 on 2022-02-12 22:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_alter_blog_image'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='blog',
            name='author',
        ),
    ]
