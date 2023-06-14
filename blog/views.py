from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# Create your views here.

def news_view(request, author_username=None):
    posts= Post.objects.filter(status=True)
    if author_username is not None:
        posts= posts.filter(author__username=author_username)
    posts = Paginator(posts,3)
    page_number = request.GET.get('page')
    try:
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.page(1)
    except EmptyPage:
        posts = posts.page(posts.num_pages)
    context={'posts': posts}
    return render(request, 'blog/news.html',context)

def single_view(request,pid):
    post=get_object_or_404(Post, id=pid, status=1)
    context={'post': post}
    return render(request, 'blog/single-news.html',context)


def archive_view(request, published_month):
    posts=Post.objects.filter(status=True, published_date__month=published_month)
    context={'posts': posts}
    return render(request, 'blog/news.html',context)

def blog_search(request):
    posts= Post.objects.filter(status=True)
    if request.method == 'GET':
        posts=posts.filter(content__contains=request.GET.get('s'))
    context={'posts': posts}
    return render(request, 'blog/news.html',context)
