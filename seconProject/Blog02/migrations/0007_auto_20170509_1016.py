# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-05-09 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Blog02', '0006_auto_20170509_0947'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='slug',
            field=models.SlugField(max_length=100, unique=True),
        ),
    ]
