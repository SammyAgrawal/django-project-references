from django.db import models

# Create your models here.

class Images(models.Model):
    name = models.CharField(max_length=100)
    picture = models.ImageField(upload_to= 'pics', blank=True, null=True)