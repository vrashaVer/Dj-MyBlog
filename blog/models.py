from django.db import models
from django.utils import timezone
import datetime

class Author(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()

    def __str__(self):
        return self.name
    


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField()
    author = models.ForeignKey(Author,on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    def published_recently(self):
        if self.published_date >= timezone.now() - datetime.timedelta(days=7):
            published_less_than_7_days_ago = True
        else: 
            published_less_than_7_days_ago = False
        return published_less_than_7_days_ago
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    author_name = models.CharField(max_length=100)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f'Comment by {self.author_name} on {self.post}'


