from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=250)
    body = models.TextField(blank=True, null=True)
    author = models.CharField(max_length=20)
    image = models.ImageField(upload_to='topicImages', blank=True, null=True)

    created = models.DateField()

    def __str__(self):
        return(self.title)

class Author(models.Model):
    name = models.CharField(max_length=20)