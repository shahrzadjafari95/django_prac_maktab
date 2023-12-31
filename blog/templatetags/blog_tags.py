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
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now())
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:  # categories= all of category
        cat_dict[name] = posts.filter(category=name).count()  # for example: {'gym':3, 'entertainment': 2 ,...}
    # sorted items according key(second item or x[1]) and maximum number(reverse = True)
    sorted_category_by_number = sorted(cat_dict.items(), key=lambda x: x[1], reverse=True)  # output:[list of tuples]
    sorted_category_by_number = dict(sorted_category_by_number[:arg])  # slice the list of tuples
    # convert_sort_category_dict = dict(sorted_category_by_number)  # convert to dictionary
    return {'categories': sorted_category_by_number}


@register.simple_tag(name='comment_count')
def function(pid):
    return Comment.objects.filter(post=pid, approved=1).count()  # this code filter comment according post.pid and
    # approved comments and then count the comments
