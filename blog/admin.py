from django.contrib import admin
from blog.models import Post
# Register your models here.



class PostAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('title','author', 'status','counted_views','created_date', 'published_date')
    list_filter=('status',)
    search_fields=['title', 'content']

   
admin.site.register(Post, PostAdmin)