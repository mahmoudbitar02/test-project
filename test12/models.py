from django.db import models

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=75)
    describtion = models.TextField(max_length=5000)
    image = models.ImageField(upload_to='test12')
