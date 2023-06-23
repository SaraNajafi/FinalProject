
from django.contrib import sitemaps
from django.urls import reverse
from blog.models import Post

class BlogSitemap(sitemaps.Sitemap):
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return Post.objects.filter(status=True)

    def lastmod(self, obj):
        return obj.published_date
