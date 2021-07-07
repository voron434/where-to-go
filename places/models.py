from enum import unique

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
    place = models.ForeignKey(Place, on_delete=models.PROTECT, related_name='images')
    file = models.ImageField(upload_to="media", width_field=None)
    priority = models.PositiveIntegerField(editable=True)

    class Meta:
        unique_together = ('place', 'priority',)

    def __str__(self):
        return f"{self.priority} {self.place.title}"
