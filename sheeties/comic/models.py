__author__ = 'francisco'

from django.db import models
from django.utils.timezone import now

class Comic(models.Model):
    image = models.ImageField(upload_to='media/comics/')
    title = models.CharField(max_length=300)
    description = models.CharField(max_length=2000)
    date_added = models.DateTimeField(default=now())