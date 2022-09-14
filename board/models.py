from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Document(models.Model):
    Did = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50)
    content = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(default=timezone.now)


class Comment(models.Model):
    Cid = models.AutoField(primary_key=True)
    Doc = models.ForeignKey('Document', on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(default=timezone.now)
