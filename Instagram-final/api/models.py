from django.db import models
from django.contrib.auth.models import User
import datetime


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    activation_key = models.CharField(max_length=40, blank=True)
    key_expires = models.DateTimeField(default=datetime.datetime.today())


class Photo(models.Model):
    class Meta:
        db_table = 'photo'
    user = models.ForeignKey(User, related_name='photos')
    image = models.ImageField()
    data = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    dislikes = models.IntegerField(default=0)


class Comment(models.Model):
    class Meta:
        db_table = 'comment'

    image = models.ForeignKey(Photo, related_name='comments', null=True, blank=True)
    user = models.ForeignKey(User, related_name='comments', null=True, blank=True)
    comment = models.TextField(verbose_name='Text comment')
    username = models.TextField(null=True, blank=True)
    data = models.DateTimeField(auto_now_add=True, blank=True, null=True)


class Like(models.Model):
    class Meta:
        db_table = 'like'

    image = models.IntegerField(null=True, blank=True)
    username = models.TextField(null=True, blank=True)


class Dislike(models.Model):
    class Meta:
        db_table = 'dislike'

    image = models.IntegerField(null=True, blank=True)
    username = models.TextField(null=True, blank=True)