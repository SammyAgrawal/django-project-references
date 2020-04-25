from django.shortcuts import render
from .models import Topic, Reply
from .forms import TopicForm, ReplyForm
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Go to /topics")

def topics(request):
    topics = Topic.objects.order_by('name')
    context = {'topics':topics}
    return render(request, 'posts/topics.html', context=context)

def replies(request, topic):
    topics = Topic.objects.filter(name=topic) #matching queryset (should only be 1 in this case)
    if(len(topics)>0):
        t = topics[0]
        queryset = Reply.objects.filter(topic=t)
        context = {'topic':t, 'replies':queryset}
    else:
        context = {'topic':topic}
    return render(request, 'posts/reply.html', context=context)

def form_view(request):
    if (request.method == 'POST'):
        tform = TopicForm(request.POST)
        rform = ReplyForm(request.POST)
        if(tform.is_valid() and rform.is_valid()):
            topic = tform.cleaned_data['topic']
            reply = rform.cleaned_data['reply']
            print(topic, "\n", reply)
    return render(request, 'posts/form.html', context={'tform':TopicForm, 'rform':ReplyForm}) 