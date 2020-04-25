from django.db import models

# Create your models here.

class User(models.Model):
    f_name = models.CharField(max_length=20)
    lname = models.CharField(max_length=20)
    email = models.EmailField(max_length=75)

    def __str__(self):
        return str(self.f_name + " " + self.lname)