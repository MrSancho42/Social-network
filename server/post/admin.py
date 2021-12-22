from django.contrib import admin

from .models import Post, PostLike


class PostAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'title', 'text', 'author', 'likes', 'creation_date')


class PostLikeAdminConfig(admin.ModelAdmin):
    list_display = ('id', 'user', 'post', 'like', 'created_at', 'updated_at')


admin.site.register(Post, PostAdminConfig)
admin.site.register(PostLike, PostLikeAdminConfig)
