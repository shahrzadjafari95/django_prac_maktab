from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Post, Category, Comment


# Register your models here.


class PostAdmin(SummernoteModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'author', 'counted_view', 'published_date', 'created_date')
    list_filter = ('status', 'published_date')
    ordering = ['created_date']
    search_fields = ['title', 'content']
    summernote_fields = ('content',)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


class CommentAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('name', 'post', 'approved', 'created_date')
    list_filter = ('post', 'approved')
    search_fields = ['name', 'post']


admin.site.register(Comment, CommentAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
