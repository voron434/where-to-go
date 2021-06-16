import os

from django.db import models
from where_to_go import settings


class Place(models.Model):
    title = models.CharField(max_length=100, blank=True)
    description_short = models.TextField(max_length=500, blank=True)
    description_long = models.TextField(blank=True)
    coord_lng = models.FloatField(null=True)
    coord_lat = models.FloatField(null=True)

    def __str__(self):
        return self.title


class Image(models.Model):
    num = 0
    link = models.ForeignKey(Place, on_delete=models.PROTECT)
    file = models.ImageField(upload_to=None, width_field=None)

    def __str__(self):
        self.num = self.num + 1
        return str(self.num) + ' ' + self.link.title
