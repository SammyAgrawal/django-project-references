from django.db import models

# Create your models here.

class School(models.Model):
    name = models.CharField(max_length=40)
    location = models.CharField(max_length=100)
    enrollment = models.IntegerField()

    def __str__(self):
        return(self.name)

class Student(models.Model):
    YEAR_CHOICES = [
        ('FR', 'Freshman'),
        ('SO', 'Sophomore'),
        ('JR', 'Junior'),
        ('SR', 'Senior'),
        ('GR', 'Graduate'),
    ]
    school = models.ForeignKey(School, on_delete=models.CASCADE)
    name = models.CharField(max_length=15)
    year = models.CharField(max_length=3, choices=YEAR_CHOICES, default='FR')

    def __str__(self):
        return(self.name)

    """
    class Meta:
        ordering = ["-name"]
    
    
    """
