# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-08-25 20:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='NewsItems',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('language', models.DateTimeField()),
                ('insert_time', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'news_data',
                'managed': True,
            },
        ),
    ]