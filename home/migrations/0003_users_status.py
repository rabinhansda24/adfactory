# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 04:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20161207_1942'),
    ]

    operations = [
        migrations.AddField(
            model_name='users',
            name='status',
            field=models.CharField(default='active', max_length=10),
        ),
    ]
