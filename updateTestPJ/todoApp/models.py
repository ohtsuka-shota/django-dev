from django.db import models

PRIORITY = (("High","high"), ("Normal","normal"), ("Low","low"))

class todoTable(models.Model):
    title = models.CharField(max_length=100)
    memo = models.TextField()
    priority = models.CharField(
        max_length=50, 
        choices= PRIORITY
        )
    deadline = models.DateField()
    
    def __str__(self):
        return self.title