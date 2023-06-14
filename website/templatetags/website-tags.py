from django import template
from blog.models import Post

register = template.Library()


@register.inclusion_tag('website/latest-news.html')
def latest_posts():
    posts = Post.objects.filter(status=True).order_by('-published_date')[:3]
    return {'posts': posts}

