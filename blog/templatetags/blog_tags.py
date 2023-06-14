from django import template
from blog.models import Post
import datetime
import calendar

register = template.Library()


@register.simple_tag(name='total_posts')
def count_posts():
    posts=Post.objects.filter(status=True, published_date__lte=datetime.datetime.now()).count()
    return posts


@register.filter
def snippet(value):
    return value[:100]

@register.inclusion_tag('blog/recent-news.html')
def recent_posts():
    posts = Post.objects.filter(status=True).order_by('-published_date')[:6]
    return {'posts': posts}



@register.inclusion_tag('blog/archive-news.html')
def archive():
    posts=Post.objects.filter(status=True)
    month_dict={}
    for i in range(12):
        month_dict[calendar.month_name[i+1]]=(posts.filter(published_date__month=i+1).count(),i+1)
    return {'month_posts': month_dict}