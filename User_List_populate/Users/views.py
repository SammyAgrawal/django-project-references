from django.shortcuts import render
from .models import User
from .forms import UserForm
from django.http import HttpResponse

# Create your views here.

def index(request):
    if (request.method == 'POST'):
        form = UserForm(request.POST)
        form.save() #instance of model
    return render(request, 'Users/index.html', context={'modelform':UserForm})

def users(request):
    queryset = User.objects.order_by('f_name')
    context = {'users': queryset}
    return render(request, 'Users/users.html', context)