from django.db import models
from aoms import settings
import datetime


# blog post model, simple one
class BlogPost(models.Model):
    post_title = models.CharField(max_length=1000)
    post_body = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.post_title


class Navigation(models.Model):
    TARGET_CHOICES = (
        ('_blank', 'BLANK'),
        ('_parent', 'PARENT'),
        ('_self', 'SELF'),
        ('_top', 'TOP'),
    )

    nav_title = models.CharField(max_length=50)
    nav_desc = models.CharField(max_length=200)
    nav_location = models.CharField(max_length=1000)
    nav_target = models.CharField(max_length=10, choices=TARGET_CHOICES)
    is_relative = models.BooleanField(default=True)
    active = models.BooleanField(default=True)
    nav_priority = models.SmallIntegerField(default=50)

    @property
    def nav_reff(self):
        reff = self.nav_location
        if self.is_relative == 1:
            reff = settings.BASE_URL + self.nav_location
        return reff

    def __str__(self):
        return self.nav_title + " -> " + self.nav_reff
