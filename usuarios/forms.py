from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserBlog

class UserBlogCreationForm(UserCreationForm):
    cpf = forms.CharField(max_length=11, required=True, help_text="Informe o CPF apenas com números")
    nome_mae = forms.CharField(max_length=100, required=False, help_text="Nome completo da mãe")
    endereco = forms.CharField(max_length=255, required=False, help_text="Endereço completo")
    nome_bairro = forms.CharField(max_length=100, required=False)
    nome_cidade = forms.CharField(max_length=100, required=False)

    class Meta:
        model = UserBlog
        fields = ('username', 'email', 'cpf', 'nome_mae', 'endereco', 
                 'nome_bairro', 'nome_cidade', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Aplicação de classes CSS
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': 'form-control'})

class UserBlogEditForm(forms.ModelForm):
    # Campos do formulário com widgets personalizados
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class': 'form-control'}))
    cpf = forms.CharField(
        max_length=11,
        required=True,
        help_text="Informe apenas números",
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_cidade = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_mae = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    endereco = forms.CharField(
        max_length=255,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )
    nome_bairro = forms.CharField(
        max_length=100,
        required=False,
        widget=forms.TextInput(attrs={'class': 'form-control'})
    )

    class Meta:
        model = UserBlog
        fields = ('username', 'email', 'cpf', 'nome_mae', 'endereco', 
                 'nome_bairro', 'nome_cidade')