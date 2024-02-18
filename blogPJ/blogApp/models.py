from django.db import models
from markdownx.models import MarkdownxField
from django.utils import timezone
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)  
    content = MarkdownxField()  
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)  
    author = models.ForeignKey(User, on_delete=models.CASCADE)  
    created_at = models.DateTimeField(default=timezone.now)  
    updated_at = models.DateTimeField(auto_now=True)  

    def __str__(self):
        return self.title