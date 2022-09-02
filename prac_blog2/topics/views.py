from django.shortcuts import render
from django.http import HttpResponse
from .models import Author, Post
from .forms import PostForm

from datetime import datetime

# Create your views here.

def index(request):

    context = {'posts' : Post.objects.all(), 'postform': PostForm}
    
    if(request.method == 'POST'):
        form = PostForm(data=request.POST) # POST dictionary with foem

        if(form.is_valid()):
            post = form.save(commit=False)
            if('image' in request.FILES):
                post.image = request.FILES['image']
            post.created = datetime.now()
            post.save()
        else:
            print(form.errors)

    return render(request, 'topics/index.html', context=context)