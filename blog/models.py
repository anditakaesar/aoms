from django.db import models
import datetime


# blog post model, simple one
class BlogPost(models.Model):
    post_title = models.CharField(max_length=1000)
    post_body = models.TextField()
    created_date = models.DateField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.post_title
