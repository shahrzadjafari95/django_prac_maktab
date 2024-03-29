from django.contrib import messages
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from website.forms import ContactForm, NewsletterForm, NameForm
from website.models import Contact


# Create your views here.


def home_view(request):
    return render(request, 'website/index.html')


def about_view(request):
    return render(request, 'website/about.html')


def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)  # request.post : input information of user that enter the form
        if form.is_valid():
            my_form = form.save(commit=False)
            my_form.name = 'unknown'
            my_form.save()
            messages.add_message(request, messages.SUCCESS, 'your ticket submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, "your ticket didn't submitted ")
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
            messages.add_message(request, messages.ERROR, 'invalid email, try again ')
            # return HttpResponseRedirect('/')  ## redirect to home page
    else:
        form = NewsletterForm()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'), {'form': form})  # redirect to same page
    # return HttpResponseRedirect('/')


def test_view(request):
    if request.method == 'POST':  # if user send data
        form = NameForm(request.POST)  # form = everything from user put in NameForm
        if form.is_valid():  # if data is valid according to the option of field
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            subject = form.cleaned_data['subject']
            message = form.cleaned_data['message']
            return HttpResponse('done')
        else:
            return HttpResponse('not done')

    form = NameForm()  # if method is get form = nameform
    return render(request, 'test.html', {'form': form})


def test_for_contact_form_with_modelform(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    form = ContactForm()
    return render(request, 'test.html', {'form': form})


def test_for_contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')  # چیزی که کاربر در فیلد نام وارد کرده است را بگیر
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        c = Contact()  # create an object that connect to the contact model
        c.name = name  # هر ایتم که از کاربر دریافت کردیم از طریق فرم در مدل کانتکت اضافه میکنیم، یعنی مثلا داخل نام
        # مدل این نامی که از کاربر گرفیتم قرار میدیم
        c.email = email
        c.subject = subject
        c.message = message
        c.save()
    return render(request, 'website/form_in_html.html')
