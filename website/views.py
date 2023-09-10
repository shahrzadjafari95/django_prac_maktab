from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render

from website.forms import ContactForm, NewsletterForm


# Create your views here.


def home_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.name = 'unknown'
            my_form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your ticket didnt submitted ')
    else:
        form = ContactForm()
    return render(request, 'website/contact.html', {'form': form})


def newsletter_view(request):
    if request.method == 'POST':
        form = NewsletterForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your message has been sent successfully')
        else:
            messages.add_message(request, messages.ERROR, 'invalid email, try again ')  # redirect to same page
            # return HttpResponseRedirect('/')  ## redirect to home page
    else:
        form = NewsletterForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    # return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':  ## if user send data
        form = NameForm(request.POST)  ## form = everything from user put in NameForm
        if form.is_valid():  ## if data is valid according to the option of field
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            return HttpResponse('done')
    else:
        form = NameForm()  ## if method is get
    return render(request, 'test.html', {'form': form})


def test_view(request):
    if request.method == 'POST':  ## if user send data
        form = ContactForm(request.POST or None)  ## form = everything from user put in NameForm
        if form.is_valid():  ## if data is valid according to the option of field
            form.save()
            # return HttpResponse('done')
        # else:
        #     return HttpResponse('not valid')
    form = ContactForm()
    return render(request, 'test.html', {'form': form})
