from django.db import models
from django.utils import timezone
import datetime

from user.models import User


class Post(models.Model):
    title = models.CharField(max_length=256)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
    creation_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title
    
    class Meta:
        db_table = 'post'


class PostLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    like = models.BooleanField(default=True)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)

    def _change_post_likes(self, is_encrease):
        if is_encrease:
            self.post.likes += 1
        else:
            self.post.likes -= 1
        self.post.save()

    def save(self, *args, **kwargs):
        """
        While object saving from view force_insert=True, so if user change
        like status, it raises IntegrityError, because it duplicates data
        """
        kwargs['force_insert'] = False
        last_like = None
        try:
            # get last user like status for this post
            last_like = PostLike.objects.filter(
                user=self.user, post=self.post).latest('created_at').like
        except PostLike.DoesNotExist:
            # if user like this post in first time
            super(PostLike, self).save(*args, **kwargs)
            self._change_post_likes(True)
            return self

        try:
            # if user changes like status today
            like = PostLike.objects.get(
                user=self.user, post=self.post, created_at__date=self.created_at)
            like.like = not like.like

            super(PostLike, like).save(*args, **kwargs)
            self._change_post_likes(like.like)

            return like
        except PostLike.DoesNotExist:
            # if user not changes like status today
            self.like = not last_like

            super(PostLike, self).save(*args, **kwargs)
            self._change_post_likes(self.like)

            return self
    
    class Meta:
        db_table = 'postlike'
