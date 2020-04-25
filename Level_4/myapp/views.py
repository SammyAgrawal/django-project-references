from django.shortcuts import render


# Create your views here.

def index(request):
    books=[
        {'title': '1984', 'author': {'name': 'George', 'age': 45}},
        {'title': 'Timequake', 'author': {'name': 'Kurt', 'age': 75}},
        {'title': 'Alice', 'author': {'name': 'Lewis', 'age': 33}},
    ]
    text = {
        "string": "well I'll be a monkey's uncle", 
        "int":100,
        "books":books,
        "list": "My dog is named FRED...BEEYATCH".split(),
        
    } 
    return render(request, 'myapp/index.html', context=text)

def other(request):
    return render(request, 'myapp/other.html')

def relative(request):
    return render(request, 'myapp/relative_url.html')