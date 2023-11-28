from django.db import models


class Book(models.Model):

    name = models.CharField(max_length=264)
    author = models.CharField(max_length=128)
    year_published = models.IntegerField()
    isbn = models.CharField(max_length=32)
