from django.contrib import admin

from .models import Category, News, Comment 

# Register your models here.

class CategoryAdmin(admin.ModelAdmin):
    pass

admin.site.register(Category,CategoryAdmin)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'text', 'category']
    list_filter = ['category']
    search_fields = ['title']
    list_editable = ['category']
    raw_id_fields = ['category']

admin.site.register(News,NewsAdmin)

class CommentAdmin(admin.ModelAdmin):
    pass

admin.site.register(Comment,CommentAdmin)
