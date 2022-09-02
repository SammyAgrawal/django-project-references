from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from django.views import View
from django.views.generic import ListView, DetailView
from django.views.generic.base import TemplateView

from .models import School, Student
# Create your views here.

class Base(View):

    def get(self, request, *args, **kwargs):
        return render(request, 'myapp/index.html', context={'message': 'from Base View'})

class Template(TemplateView):
    template_name = "myapp/index.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Straght outta Template View'
        return(context)

class List(ListView):
    #model = School # this equals queryset=objects.all()
    queryset = School.objects.order_by('enrollment')
    template_name = 'myapp/school_list.html'
    context_object_name = 'schools'

class Detail(DetailView):
    model = School # this equals queryset=objects.all()
    
    context_object_name = 'school'
    #template_name = 'myapp/school_detail.html' #implied

    def dispatch(self, request, *args, **kwargs):
        dis =  super().dispatch(request, *args, **kwargs)

        print(kwargs.get('pk'))
        
        return(dis)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['message'] = 'Detail View render'

        #print(context)
        #print(self.number)

        return(context)

#https://docs.djangoproject.com/en/3.0/topics/class-based-views/generic-display/#

class DetailName(DetailView):
    model = School
    context_object_name = 'school'

    def get_object(self):
        self.school = get_object_or_404(School, name=self.kwargs['name'])
        return(School.objects.filter(name=self.kwargs['name']))
