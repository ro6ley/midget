from __future__ import unicode_literals
from django.db import models
import datetime


# Create your models here.
class Link(models.Model):
    """
    This class defines the model to handle links
    """
    title = models.CharField(max_length=255, blank=True, null=True)
    short_url = models.CharField(max_length=255)
    long_url = models.CharField(max_length=255)
    date_created = models.DateTimeField(auto_now_add=True, blank=True)
    date_modified = models.DateTimeField(auto_now=True, blank=True)

    def __unicode__(self):
        return self.title

    def to_json(self):
        return {
            'id': self.id,
            'title': self.title,
            'long_url': self.long_url,
            'short_url': self.short_url,
            'date_created': self.date_created,
            'date_modified': self.date_modified            
        }
