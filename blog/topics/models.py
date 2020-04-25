from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=120, blank=False, unique=True)
    content = models.TextField(max_length=5000)
    date_published = models.DateField()
    def __str__(self):
        return self.title

class Reply(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    content = models.TextField(max_length=1200)