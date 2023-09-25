from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect


# Create your views here.


def login_view(request):
    if not request.user.is_authenticated:  # this user dont login to panel
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")  # username = The thing that the user entered
                password = form.cleaned_data.get("password")  # password = The thing that the user entered
                user = authenticate(request, username=username, password=password)  # we create an object of user input
                if user is not None:  # if exists
                    login(request, user)  # user login to site
                    return redirect('/')  # redirect to home page
        else:  # if request.method == get ( this means click on the login url )
            form = AuthenticationForm()
            context = {'form': form}
            return render(request, 'accounts/login.html', context)  # show login page
    else:  # if user login in site
        return redirect('/')  # redirect to home page


def logout_view(request):
    pass


def signup_view(request):
    return render(request, 'accounts/signup.html')
