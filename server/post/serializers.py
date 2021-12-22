from rest_framework import serializers

from .models import Post, PostLike


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ('id', 'title', 'text', 'author', 'likes', 'creation_date')
        read_only_fields = ('id', 'author', 'likes', 'creation_date')


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostLike
        fields = ('user', 'post', 'like')
        read_only_fields = ('user', 'like')
