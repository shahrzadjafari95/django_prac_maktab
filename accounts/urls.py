from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [
    # login url
    path('login/', views.login_view, name='login'),
    # logout url
    path('logout/', views.logout_view, name='logout'),
    # registration url
    path('signup/', views.signup_view, name='signup'),
]
