from django.urls import path
from blog.views import *

app_name = 'blog'

urlpatterns = [path('', blog_view, name='index'),
               path('single-<int:pid>', single_view, name='single'),
               # path('name/<str:name>/lastname/<str:family>/age/<str:age>/', test, name='test'),
               # path('post-<int:pid>/', test2, name='test'),
               # path('post--<int:pid>/', test3, name='test'),

               ]
