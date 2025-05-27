from django import forms
from django.contrib.auth.models import User
from .models import Profile, Submission

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model = User
        fields = ['username', 'email', 'password'] 


class SubmitForm(forms.ModelForm):
    class Meta:
        model=Submission
        fields=['author', 'photo', 'caption']
        