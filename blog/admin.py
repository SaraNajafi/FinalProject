from django.contrib import admin
from blog.models import Post, Comment
from django_summernote.admin import SummernoteModelAdmin
# Register your models here.



class PostAdmin(SummernoteModelAdmin):
    date_hierarchy='created_date'
    list_display=('title','author', 'status','counted_views','created_date', 'published_date')
    list_filter=('status',)
    search_fields=['title', 'content']
    summernote_fields= ('content',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy='created_date'
    list_display=('name','subject','email','created_date', 'updated_date', 'approved')
    search_fields=['name', 'post']

admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)