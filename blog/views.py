from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404
from django.utils import timezone

from blog.models import Post


# Create your views here.


# def blog_view(request):
#     posts = Post.objects.filter(status=1)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)

## practice 1.1 in chapter6
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    posts = Paginator(posts, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


## practice 1.2 in chapter6
# def single_view(request, pid):
#     post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
#     post.counted_view += 1
#     post.save()
#     context = {'post': post}
#     return render(request, 'blog/blog-single.html', context)

### practice 2 in chapter6
def single_view(request, pid):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    post.counted_view += 1
    post.save()
    context = {'post': post,
               'next': posts.filter(id__gt=post.id).order_by('id').first(),
               'previous': posts.filter(id__lt=post.id).order_by('-id').first()
               }
    return render(request, 'blog/blog-single.html', context)


def blog_category(request, cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def test_view(request, name):
    return render(request, 'test.html')
