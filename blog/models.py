from django.db import models


# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField(max_length=1000)
    date_create = models.DateTimeField(auto_now_add=True)
    date_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
