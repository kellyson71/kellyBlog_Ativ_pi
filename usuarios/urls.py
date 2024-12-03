from django.urls import path
from .views import login_view, logout_view, register, lista_usuarios, cadastrar_usuario, editar_usuario

app_name = 'usuarios'

# Definição das rotas do aplicativo de usuários
urlpatterns = [
    # Autenticação
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    
    # Gerenciamento de usuários
    path('listar/', lista_usuarios, name='lista_usuarios'),
    path('cadastrar/', cadastrar_usuario, name='cadastrar_usuario'),
    path('register/', register, name='cadastrar_usuario'),
    path('atualizar/<int:id>', editar_usuario, name='editar_usuario'),    
]
