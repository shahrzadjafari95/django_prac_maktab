from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login_view, name='login'),  # login url

    path('logout/', views.logout_view, name='logout'),  # logout url

    path('signup/', views.signup_view, name='signup'),  # registration url
]
