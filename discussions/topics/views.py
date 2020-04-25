from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    context = {"random_stuff": "MOMMAYYYYYYYYY"}
    return render(request, 'topics/index.html', context)