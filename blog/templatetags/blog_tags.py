from django import template
from django.utils import timezone

from blog.models import Post, Category

register = template.Library()


@register.simple_tag()
def say_hello():
    return 'hello shahrzad'


@register.simple_tag()
def function(a=8):
    return a + 2


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


@register.inclusion_tag('popularpost.html')
def popularpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')[:3]
    return {'posts': posts}


@register.inclusion_tag('blog/blog-poppost.html')
def latest_post(arg=3):
    posts = Post.objects.filter(status=1).order_by('published_date')[:arg]
    return {'posts': posts}

# this code write for blog-post-categories.html and this code use in this page, after that use it,
# we can use code in main page
@register.inclusion_tag('blog/blog-post-categories.html')
def post_categories():
    posts = Post.objects.filter(status=1)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'categories': cat_dict}