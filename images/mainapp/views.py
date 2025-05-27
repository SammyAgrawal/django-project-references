from django.shortcuts import render
from .forms import ImageForm
from .models import Images
# Create your views here.

def index(request):
    images = Images.objects.all()

    c = {
        'image_form': ImageForm(),
        'db_images' : images,
    }

    if request.method == "POST": #form
        print("FORM received")
        print(request.FILES)
        form = ImageForm(data=request.POST)

        if (form.is_valid()):
            print("VALID FORM")
            image = form.save(commit=False)

            print(request.FILES)
            print()

            if ('picture' in request.FILES):
                print("HAS IMAGE")
                image.picture = request.FILES['picture']

            image.save()
        else:
            print("Invalid Form")
            print(form.errors)
    return render(request, 'main.html', context=c)