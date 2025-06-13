from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    twitter_token = models.CharField(max_length=255, blank=True)
    facebook_token = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return self.username
    
class Post(models.Model):
    PLATFORM_CHOICES = [('twitter', 'Twitter'), ('facebook', 'Facebook')]
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    platform = models.CharField(max_length=20, choices=PLATFORM_CHOICES)
    content = models.TextField()
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)
    created_at = models.DateTimeField()
    
    def __str__(self):
        return f"{self.platform} post by {self.user.username}"