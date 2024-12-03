from django.db import models
from django.contrib.auth.models import AbstractUser

class UserBlog(AbstractUser):
    nome_mae = models.CharField(max_length=100, blank=True, null=True)
    cpf = models.CharField(max_length=11, unique=True, verbose_name="Cadastro de Pessoa Física")
    endereco = models.CharField(max_length=255, blank=True, null=True)
    nome_bairro = models.CharField(max_length=100, blank=True, null=True)
    nome_cidade = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"{self.cpf} - {self.username}"