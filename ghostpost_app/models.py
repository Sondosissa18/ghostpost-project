from django.db import models
# from django.utils.timezone import datetime 
from django.utils import timezone  


class GhostPost(models.Model):
    text = models.CharField(max_length=100)
    ghostpost=models.BooleanField()
    upvote = models.IntegerField(default=0)
    downvote = models.IntegerField(default=0)
    created_at = models.DateTimeField(default=timezone.now)
    
    def __str__(self):
        return f"{self.text}"
