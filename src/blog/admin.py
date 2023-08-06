from django.contrib import admin
from .models import Article

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'status', 'author', 'slug')
    prepopulated_fields = {'slug': ('title',), }
    search_fields = ('title', 'status')
