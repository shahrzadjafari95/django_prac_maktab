from django.urls import path

from blog.views import *

app_name = 'blog'

urlpatterns = [path('', blog_view, name='index'),
               path('post<int:pid>/', single_view, name='single'),
               path('test<str:name>/', test_view, name='test'),
               path('category/<str:cat_name>/', blog_view, name='category'),
               path('tag/<str:tag_name>/', blog_view, name='tag'),
               path('author/<str:author_username>/', blog_view, name='author'),
               path('search/', blog_search, name='search', )
               ]
