from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Profile(models.Model):
    """
    user has: first_name, last_name,  username, email, password
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    has_voted = models.BooleanField(default=False)
    def __str__(self):
        return (self.user.first_name + self.user.last_name)


class Submission(models.Model):
    author = models.ForeignKey(Profile, on_delete=models.CASCADE) #temp on_delete
    photo = models.ImageField(upload_to='submissions', blank=True)
    caption = models.CharField(max_length=100, blank=True, null=True)
    votes = models.IntegerField(default=0, null=False)
    def __str__(self):
        return(self.author.user.username)