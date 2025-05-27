from django.contrib import admin
from .models import School, Student
# Register your models here.

models = [School, Student]

for model in models:
    admin.site.register(model)
