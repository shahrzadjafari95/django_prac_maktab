from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


# Create your views here.


# def blog_view(request):
#     posts = Post.objects.filter(status=1)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)

## practice 1.1 in chapter6
def blog_view(request):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


## practice 1.2 in chapter6
# def single_view(request, pid):
#     post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
#     post.counted_view += 1
#     post.save()
#     context = {'post': post}
#     return render(request, 'blog/blog-single.html', context)


def single_view(request, pid):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    post = get_object_or_404(Post, pk=pid)
    context = {'post': post,
               'next': posts.filter(id__gt=post.id).order_by('id').first(),
               'previous': posts.filter(id__lt=post.id).order_by('-id').first()
               }
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
