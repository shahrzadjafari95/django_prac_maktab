from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    # login url
    path('login/', views.login_view, name='login'),
