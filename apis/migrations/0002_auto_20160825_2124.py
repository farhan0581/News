# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 21:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apis', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newsitems',
            name='language',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='newsitems',
            name='title',
            field=models.CharField(max_length=100),
        ),
    ]