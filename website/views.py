from django.shortcuts import render
from django.http import HttpResponse, JsonResponse


# Create your views here.


def home_view(request):
    return HttpResponse('<h1> Hello this is Home Page.</h1>')


def about_view(request):
    return HttpResponse('<h1> Hello this is About Page.</h1>')


def contact_view(request):
    return HttpResponse('<h1> Hello this is Contact Page.</h1>')
