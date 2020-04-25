from django.urls import path, include
from . import views

# NEW: TEMPLATE TAGGING
app_name = 'myapp'

urlpatterns = [
    path('', views.index, name='home'),
    path('other/', views.other, name='other'),
    path('relative/', views.relative, name='relative'),   
]