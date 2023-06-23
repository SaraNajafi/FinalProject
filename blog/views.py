from django.shortcuts import render,get_object_or_404
from blog.models import Post, Comment
from blog.forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages

# Create your views here.

def news_view(request, author_username=None, **kwargs):
    posts= Post.objects.filter(status=True)
    if author_username is not None:
        posts= posts.filter(author__username=author_username)
    if kwargs.get('tag_name') != None:
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.add_message(request, messages.SUCCESS, 'Your comment have been submitted Successfully')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment did not submitted.')   
    post=get_object_or_404(Post, id=pid, status=1)
    comments = Comment.objects.filter(post=post.id, approved=True).order_by('-created_date')
    form = CommentForm()
    context={'post': post, 'comments': comments, 'form': form}
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
