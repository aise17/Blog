# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 09:47
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog02', '0005_comment_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(),
        ),
    ]
