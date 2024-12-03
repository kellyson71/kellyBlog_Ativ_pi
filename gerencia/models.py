from django.db import models
from usuarios.models import UserBlog

# Modelo para categorização de notícias
class Categoria(models.Model):
    nome = models.CharField(max_length=100, unique=True)
    
    def __str__(self):
        return self.nome

# Modelo para armazenamento de notícias
class Noticia(models.Model):
    titulo = models.CharField(max_length=100)
    texto = models.TextField()
    data_publicacao = models.DateField(auto_created=True)
    usuario = models.ForeignKey(UserBlog, on_delete=models.CASCADE, blank=True, null=True)
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='noticias/')


