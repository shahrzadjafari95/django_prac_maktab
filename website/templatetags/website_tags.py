from django import template
from django.utils import timezone

from blog.models import Post

register = template.Library()


@register.inclusion_tag("website/website-recentpost.html")
def recent_post():
    posts = Post.objects.filter(status=1, published_date__lte=timezone.now()).order_by('-published_date')[:6]
    return {'posts': posts}
