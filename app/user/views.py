from django.shortcuts import render


# Create your views here.
def signup_func(request):
    return render(request, "user/signup.html", context={})
