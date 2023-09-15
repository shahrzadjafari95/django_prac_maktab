from django.contrib import admin

from .models import Post, Category


# Register your models here.


class PostAdmin(admin.ModelAdmin):
    date_hierarchy = 'created_date'
    empty_value_display = '-empty-'
    list_display = ('title', 'status', 'author', 'counted_view', 'published_date', 'created_date')
    list_filter = ('status', 'published_date')
    ordering = ['created_date']
    search_fields = ['title', 'content']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'id',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)
