from django.urls import path

from website.views import *

app_name = 'website'

urlpatterns = [path('', home_view, name='index'),
               path('about/', about_view, name='about'),
               path('contact/', contact_view, name='contact'),
               path('test/', test_for_contact_form_with_modelform, name='test'),
               path('newsletter/', newsletter_view, name='newsletter'),
               ]
