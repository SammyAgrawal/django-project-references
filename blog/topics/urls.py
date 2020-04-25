from django.urls import path
from . import views

urlpatterns = [
    path('', views.topics, name='posts'),

    path('<str:topic>/', views.post) #keep last
]