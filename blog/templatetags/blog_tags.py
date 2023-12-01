from django import template
from django.utils import timezone

from blog.models import Post, Category, Comment

register = template.Library()


@register.simple_tag()
def say_hello():
    return 'hello shahrzad'


@register.simple_tag()
def function(a, b=4):  # we can set default value for argument or not set
    return a + 2 + b


@register.simple_tag(name='count_total_posts')
def function():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).count()
    return posts


@register.simple_tag(name='total_posts')
def function():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    return posts


@register.filter
def snippets(value):
    return value[:10]


# This tag shows posts according to the latest posts that have been published
@register.inclusion_tag('blog/blog-latest.html')
def latest_post():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:3]
    return {'posts': posts}


# This tag shows posts according to the maximum view
@register.inclusion_tag('blog/blog-popular_post.html')
def popular_post(arg=3):
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-counted_view')[:arg]
    return {'posts': posts}


# this code write for blog-post-categories.html and use in this page, after that use it,
# we can use code in main page
@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories(arg=5):
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    ## sorted items according key(secont item or x[1])
    sorted_category_by_number = sorted(cat_dict.items(), key=lambda x: x[1], reverse=True)
    converted_dict = dict(sorted_category_by_number)
    converted_dict = dict(list(converted_dict.items())[:arg])
    return {'categories': converted_dict}


@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=1).count()  ## this code filter post according pid and approved
