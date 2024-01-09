from django.contrib import messages
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect


# Create your views here.

def login_view(request):
    if not request.user.is_authenticated:  # this user not login to panel
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                username = form.cleaned_data.get("username")  # username = The thing that the user entered
                password = form.cleaned_data.get("password")  # password = The thing that the user entered
                user = authenticate(request, username=username, password=password)  # we create an object of user input
                if user is not None:  # if exists
                    login(request, user)  # login user to site
                    return redirect('/')  # after login redirect to home page
        # if request.method = get ( this means click on the login url )
        form = AuthenticationForm()  # show the login form to the user
        context = {'form': form}
        return render(request, 'accounts/login.html', context)  # show login page
    else:  # if user login in site
        return redirect('/')  # redirect to home page


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signup_view(request):
    if not request.user.is_authenticated:  # if user not login in panel
        if request.method == 'POST':  # if user post the information from form
            form = UserCreationForm(request.POST)  # the form fill of user information input
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('/accounts/login')  # redirect to login page
            else:
                messages.add_message(request, messages.ERROR, "you didn't registered ")
                return redirect('/')
        else:
            form = UserCreationForm()  # if request.method = get that's mean user click to sing up url
            context = {'form': form}
            return render(request, 'accounts/signup.html', context)  # we show signup page
    else:
        return redirect('/')
