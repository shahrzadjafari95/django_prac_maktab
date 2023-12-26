from django.contrib import messages
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone

from blog.forms import CommentForm
from blog.models import Post, Comment


# Create your views here.


# def blog_view(request):
#     posts = Post.objects.filter(status=1)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)


# practice 1.1 in chapter6
def blog_view(request, **kwargs):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')
    if kwargs.get('cat_name') is not None:
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_username') is not None:
        posts = posts.filter(author__username=kwargs['author_username'])
    if kwargs.get('tag_name') is not None:
        posts = posts.filter(tag__name__in=[kwargs['tag_name']])
    posts = Paginator(posts, 3)  # posts that filter by above conditions
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:  # if user enter a string or not int object
        posts = posts.get_page(1)  # return page1
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
    if request.method == "POST":
        form = CommentForm(request.POST)  # if user send a comment for blog
        if form.is_valid():
            form.save()
            # this message show in admin panel after submitted comment
            messages.add_message(request, messages.SUCCESS, 'your comment submitted successfully')
        else:
            messages.add_message(request, messages.ERROR, 'your comment didnt submitted ')
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())  # for posts that have these conditions
    # post = get_object_or_404(Post, pk=pid, status=1, published_date__lte=timezone.now())
    post = get_object_or_404(posts, pk=pid)
    if not post.login_require:  # if login require don't need (that's mean we can see every thing in blog single)
        # show the comment that approved in admin panel and order by last comment
        comments = Comment.objects.filter(post=post.id, approved=1).order_by('-created_date')
        form = CommentForm()  # if request.method = get we show comment form to single page
        post.counted_view += 1
        post.save()
        context = {'post': post,
                   'next': posts.filter(id__gt=post.id).order_by('id').first(),
                   'previous': posts.filter(id__lt=post.id).order_by('-id').first(),
                   'comments': comments,
                   'form': form
                   }
        return render(request, 'blog/blog-single.html', context)
    else:
        return redirect('/accounts/login/')


# def blog_category(request, cat_name):
#     posts = Post.objects.filter(status=1)
#     posts = posts.filter(category__name=cat_name)
#     context = {'posts': posts}
#     return render(request, 'blog/blog-home.html', context)


def blog_search(request):
    posts = Post.objects.filter(status=1)
    print(request.__dict__)
    if request.method == 'GET':
        posts = posts.filter(content__contains=request.GET.get('s'))
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)


def test_view(request, name):
    post = Post.objects.get(title=name)
    context = {'post': post}
    return render(request, 'test.html', context)
