from django.db import models
from django.contrib.auth.models import User

PRIORITY = (("High","high"), ("Normal","normal"), ("Low","low"))

class todoTable(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50, 
        choices= PRIORITY
        )
    deadline = models.DateField()
    
    def __str__(self):
        return self.title