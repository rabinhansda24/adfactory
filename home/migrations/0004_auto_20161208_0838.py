# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-12-08 08:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_users_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='mediatype',
            name='mediaType',
            field=models.CharField(max_length=20, unique=True),
        ),
    ]