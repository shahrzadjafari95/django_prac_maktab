from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from blog.models import Post


class BlogSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(self):
        return Post.objects.filter(status=True)

    def location(self, item):
        return reverse('blog:single', kwargs={'pid': item.pk})
