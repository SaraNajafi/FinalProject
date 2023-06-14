from django.contrib import admin
from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('', news_view, name='news'),
    path('post-<int:pid>', single_view, name='single'),
    path('archive/<int:published_month>', archive_view, name='archive'),
    path('author/<str:author_username>', news_view, name='author'),
    path('search/', blog_search, name='search'),
    
]