# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-17 10:16
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('operation', '0005_script_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='script',
            name='author',
            field=models.CharField(default='noAuthor', max_length=100),
        ),
    ]
