from django.db import models

# Create your models here.

class Topic(models.Model):
    name = models.CharField(max_length=75, unique=True)

    def __str__(self):
        return self.name

class Discussion(models.Model):
    topic = models.ForeignKey(Topic, on_delete = models.CASCADE)
