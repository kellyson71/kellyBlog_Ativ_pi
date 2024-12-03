from django.urls import path
from .views import *

app_name = 'gerencia'

# Configuração das URLs do módulo de gerenciamento
urlpatterns = [
    # Página inicial
    path('', inicio_gerencia, name='gerencia_inicial'),
    
    # Gerenciamento de notícias
    path('noticias/listar/', listagem_noticia, name='listagem_noticia'),
    path('noticias/nova/', cadastrar_noticia, name='cadastro_noticia'),
    path('noticias/modificar/<int:id>', editar_noticia, name='editar_noticia'),
    path('noticias/excluir/<int:id>', excluir_noticia, name='excluir_noticia'),
    
    # Gerenciamento de categorias
    path('categoria/listar/', listagem_categoria, name='listagem_categoria'),
    path('categoria/nova/', cadastrar_categoria, name='cadastro_categoria'),
    path('categoria/modificar/<int:id>', editar_categoria, name='editar_categoria'),
    path('categoria/excluir/<int:id>', excluir, name='excluir'),
]