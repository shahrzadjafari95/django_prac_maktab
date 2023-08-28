from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [path('', blog_view, name='index'),
               path('post-<int:pid>/', single_view, name='single'),
               path('name/<str:name>/', test_view, name='test'),
               path('category/<str:cat_name>', blog_category, name='category'),
               ]
