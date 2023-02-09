from django.db import models
from apps.post.models import Post
# Create your models here.

class Comentario(models.Model):
    comentario =models.TextField()
    fecha = models.DateField(auto_now=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)