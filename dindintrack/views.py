from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Transacao
from django.contrib.auth.models import User


class ControleFinanceiro(View):
    def get(self, request):
        transacoes = Transacao.objects.all()
        return render(request, 'tela_principal.html', {'transacoes': transacoes})
    
    def post(self, request):
        usuario = self.request.user
        descricao = request.POST.get('descricao')
        valor = request.POST.get('valor')
        tipo = request.POST.get('tipo')

        Transacao.objects.create(
            usuario = usuario,
            descricao = descricao,
            valor = valor,
            tipo = tipo,
        )

        return redirect('render_create')

