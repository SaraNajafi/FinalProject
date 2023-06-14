from django.shortcuts import render,get_object_or_404
from blog.models import Post

# Create your views here.

def news_view(request):
    posts= Post.objects.filter(status=True)
    context={'posts': posts}
    return render(request, 'blog/news.html',context)

def single_view(request,pid):
    post=get_object_or_404(Post, id=pid, status=1)
    context={'post': post}
    return render(request, 'blog/single-news.html',context)