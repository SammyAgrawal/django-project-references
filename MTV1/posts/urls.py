from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.topics, name='topics'),
    path('form/', views.form_view, name='form'),
    path('<str:topic>/', views.replies, name='replies'),
]