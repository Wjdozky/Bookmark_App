from django.db import models

class Post(models.Model):
    name=models.TextField(null=True)
    content=models.TextField()
