from django.contrib import admin
from django.urls import path
from blog.views import *


app_name = 'blog'

urlpatterns = [
    path('', news_view, name='news'),
    path('post-<int:pid>', single_view, name='single'),
    
]