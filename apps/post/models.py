from django.db import models

class Categoria(models.Model):
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=250, null=False)
       
    def __str__(self):
        return self.nombre
    
# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=250, null=False)
    fecha = models.DateTimeField(auto_now_add=True)
    texto = models.TextField(null=True)
    activo = models.BooleanField(default=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.RESTRICT, null=True)
    imagen = models.ImageField(upload_to='post', default='post/default')

    

    def __str__(self):
        return self.titulo