from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect


# Create your views here.


def login_view(request):
    if request.method == "POST":
        username = request.POST["username"]  # Something that user enter in login form
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)  # Checks in the db whether it exists or not
        if user is not None:  # if exists
            login(request, user)
            return redirect('/blog/category/entertainment/')  # redirect to home page
    return render(request, 'accounts/login.html')


def logout_view(request):
    pass


def signup_view(request):
    return render(request, 'accounts/signup.html')
