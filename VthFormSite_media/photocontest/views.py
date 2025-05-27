from django.shortcuts import render
from .models import Profile, Submission
from .forms import SubmitForm, UserForm
# Create your views here.

def photo(request):
    context = {"submitform": SubmitForm, "photos":Submission.objects.all()}
    #context["Submitted"] = True
    if (request.method == "POST"):
        #new submission added
        submission = SubmitForm(data=request.POST)
        if (submission.is_valid()):
            print("REACHED")
            submission_object = submission.save(commit=False) # model instance
            if('photo' in request.FILES):
                submission_object.photo = request.FILES['photo']
            submission_object.save()
            context["Submitted"] = True
        else:
            print(submission.errors)

    return render(request, 'photocontest/index.html', context=context)

def login(request):
    registered=False
    userform = UserForm

    if(request.method == "POST"):
        userform = UserForm(data=request.POST)

        if (userform.is_valid()):
            user = userform.save()
            user.set_password(user.password)
            user.save()
            prof = Profile(user=user, has_voted=False)
            prof.save()
            registered=True
    return render(request, 'photocontest/registration.html', {"registered":registered, "ProfileForm": userform})



