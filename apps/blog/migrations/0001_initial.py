# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-16 16:53
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, unique=True)),
                ('url', models.CharField(max_length=255, unique=True)),
                ('description', models.TextField()),
                ('body', models.TextField()),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('release_time', models.DateTimeField(default='1970-1-1 00:00:00')),
                ('status', models.CharField(choices=[('0', '发布'), ('1', '存稿')], default=0, max_length=1)),
                ('read', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Categories',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('url', models.URLField(unique=True)),
                ('description', models.CharField(default='此用户没有添加任何描述', max_length=255)),
                ('add_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=80)),
                ('keywords', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=200)),
                ('nickname', models.CharField(max_length=100)),
                ('avatar', models.ImageField(upload_to='%Y/%m')),
                ('homedescription', models.CharField(max_length=150)),
                ('recordinfo', models.CharField(max_length=100)),
                ('statisticalcode', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('created_time', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.AddField(
            model_name='article',
            name='categories',
            field=models.ManyToManyField(to='blog.Categories'),
        ),
        migrations.AddField(
            model_name='article',
            name='tag',
            field=models.ManyToManyField(to='blog.Tag'),
        ),
    ]
