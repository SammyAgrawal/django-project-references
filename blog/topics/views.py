from django.shortcuts import render
from .models import Post, Reply
from .forms import PostForm, ReplyForm
from datetime import datetime
# Create your views here.

def index(request):
    return render(request, 'topics/index.html')

def topics(request):
    query = Post.objects.order_by('date_published')
    if (request.method == 'POST'):
        # new reply added
        post = Post(date_published=datetime.now())
        form = PostForm(request.POST, instance=post)
        form.save()


    return render(request, 'topics/topics.html', context = {'posts':query, 'postform':PostForm})

def post(request, topic):
    match = Post.objects.filter(title=topic)
    context = {'form':ReplyForm}
    if len(match)>0: #if there is a matching post
        post_match = match[0] #only one matching post (unique)
        replies = Reply.objects.filter(post=post_match)
        context = {'post':post_match, 'replies':replies, 'form':ReplyForm}
    if (request.method == 'POST'):
        # new reply added
        form = ReplyForm(request.POST)
        #if (form.is_valid()):
            
    return render(request, 'topics/post.html', context=context)
    