from django.contrib.auth.views import (
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView
)
from django.urls import path

from . import views

app_name = 'accounts'

urlpatterns = [

    path('login/', views.login_view, name='login'),  # login url

    path('logout/', views.logout_view, name='logout'),  # logout url

    path('signup/', views.signup_view, name='signup'),  # registration url

    path('password-reset/', PasswordResetView.as_view(template_name='registration/password_reset_form.html'),
         name='password-reset'),

    path('password-reset/done/', PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'),
         name='password_reset_done'),

    path('password-reset-confirm/<uidb64>/<token>/',
         PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.css'),
         name='password_reset_confirm'),

    path('password-reset-complete/',
         PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'),
         name='password_reset_complete'),
]
