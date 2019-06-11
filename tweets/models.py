from django.db import models

from users.models import User


class Tweet(models.Model):
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    country = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)

class HashTag(models.Model):
    name = models.CharField(max_length=20, unique=True)
    tweet = models.ManyToManyField(Tweet)

    def __unicode__(self):
        return self.name
