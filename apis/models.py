from __future__ import unicode_literals
from django.db import models


class NewsItems(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    language = models.CharField(max_length=50)
    insert_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = True
        db_table = 'news_data'
        ordering = ['-insert_time']

    def create(self, validated_data):
        return NewsItems.objects.create(**validated_data)
