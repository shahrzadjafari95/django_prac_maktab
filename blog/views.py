from django.shortcuts import render, get_object_or_404
from blog.models import Post
from datetime import datetime


# Create your views here.


# def blog_view(request):
#     posts = Post.objects.filter(status=1)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)


def blog_view(request):
    current_time = datetime.now()
    posts = Post.objects.filter(published_date__lte=current_time)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def single_view(request, pid):
    post = get_object_or_404(Post, pk=pid)
    if post:
        post.counted_view += 1
        post.save()
    context = {'post': post}
    return render(request, 'blog/blog-single.html', context)

## for test
# def test(request, name, family, age):
#     context = {'name': name, 'family': family, 'age': age}
#     return render(request, 'test.html', context)


# def test2(request, pid):
#     context = {'pid': pid}
#     return render(request, 'test.html', context)


# def test3(request, pid):
#     post = get_object_or_404(Post, pk=pid)
#     context = {'post': post}
#     return render(request, 'test.html', context)
