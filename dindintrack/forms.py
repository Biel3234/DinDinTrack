from django.contrib.auth.models import User
from .models import Cartao
from django import forms

class FormularioCadastro(forms.ModelForm):
    class Meta:
        model = User

        fields = ['username', 'email', 'password']

        labels = {
                  'username': 'Nome de Usuario',
                  'email': 'E-mail',
                  'password': 'Senha'
                  }
        
        widgets = {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
        }

class FormularioCadastroCartao(forms.ModelForm):
    class Meta:
        model = Cartao

        fields = ['nome', 'descricao', 'limite', 'vencimento_fatura', 'fechamento_fatura']

        labels = {
            'nome': 'Nome do cartão',
            'descricao': 'Descrição',
            'limite': 'Limite do cartão',
            'vencimento_fatura': 'Data de vencimento da fatura',
            'fechamento_fatura': 'Data de fechamento da fatura',

        }

        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control'}),
            'limite': forms.NumberInput(attrs={'class': 'form-control'}),
            'vencimento_fatura': forms.NumberInput(attrs={'class': 'form-control'}),
            'fechamento_fatura': forms.NumberInput(attrs={'class': 'form-control'}),
        }