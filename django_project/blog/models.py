from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models (Databases) here.

# Each class is going to be its own table in the database
# Advantage of this - you dont need to knowno SQL to create the Post database


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    objects = models.Manager()
    
    def __str__(self):
        return self.title