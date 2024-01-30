from django.contrib import messages, auth
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect

from .forms import NewUserForm


# Create your views here.

# def login_view(request):
#     if not request.user.is_authenticated:  # this user not login to panel
#         if request.method == "POST":
#             form = AuthenticationForm(request=request, data=request.POST)
#             if form.is_valid():
#                 username = form.cleaned_data.get("username")  # username = The thing that the user entered
#                 password = form.cleaned_data.get("password")  # password = The thing that the user entered
#                 user = authenticate(request, username=username, password=password)  # we create an object of user input
#                 if user is not None:  # if exists
#                     login(request, user)  # login user to site
#                     return redirect('/')  # after login redirect to home page
#         # if request.method = get ( this means click on the login url )
#         form = AuthenticationForm()  # show the login form to the user
#         context = {'form': form}
#         return render(request, 'accounts/login.html', context)  # show login page
#     else:  # if user login in site
#         return redirect('/')  # redirect to home page
#

# in this method user can log in with email or username
def login_view(request):
    if not request.user.is_authenticated:  # the user don't log in to panel
        if request.method == 'POST':  # if user enter the information to log in form
            userinput = request.POST['username']  # userinput = username that user input in
            try:
                username = User.objects.get(email=userinput)  # if user enter email in form
            except User.DoesNotExist:
                username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password)  # we create an object of user input

            if user is not None:  # if user is existed
                auth.login(request, user)  # login user
                return redirect('/')  # redirect to home page
            else:
                messages.add_message(request, messages.ERROR, 'username or password not correct, try again')
                return redirect('/accounts/login/')

        return render(request, "accounts/login.html")  # if request.method = get show login page
    else:
        return redirect('/')  # if user is log in redirect to home page


@login_required
def logout_view(request):
    logout(request)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def signup_view(request):
    if not request.user.is_authenticated:  # if user not login in panel
        if request.method == 'POST':  # if user post the information from form
            form = NewUserForm(request.POST)  # the form fill of user information input
            if form.is_valid():
                form.save()
                messages.success(request, 'Account created successfully')
                return redirect('/accounts/login')  # redirect to login page
            else:
                messages.add_message(request, messages.ERROR, "you didn't registered ")
                return redirect('/')
        form = NewUserForm()  # if request.method = get that's mean user click to sing up url
        context = {'form': form}
        return render(request, 'accounts/signup.html', context)  # we show signup page
    else:
        return redirect('/')
