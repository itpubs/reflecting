# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-07-17 10:21
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='release_time',
        ),
        migrations.AddField(
            model_name='article',
            name='updated_time',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
