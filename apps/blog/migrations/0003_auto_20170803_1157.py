# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-08-03 11:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_auto_20170717_1021'),
    ]

    operations = [
        migrations.AlterField(
            model_name='setting',
            name='avatar',
            field=models.ImageField(blank=True, null=True, upload_to='%Y/%m'),
        ),
        migrations.AlterField(
            model_name='setting',
            name='description',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='homedescription',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='keywords',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='nickname',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='recordinfo',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='statisticalcode',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='setting',
            name='title',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
    ]