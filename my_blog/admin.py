from django.contrib import admin

from my_blog.models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ['pk', 'name', 'slug', 'description', 'image']
