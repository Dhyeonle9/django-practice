from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    content = models.CharField(max_length=100)
    updated_at = models.DateTimeField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
