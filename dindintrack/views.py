from django.shortcuts import render, redirect
from django.views.generic import View
from .models import Transacao
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse


class ControleFinanceiro(LoginRequiredMixin, View):
    login_url = 'login'
    def get(self, request):
        perfil = self.request.user
        transacoes = perfil.transacoes.all()
        saldo = 0
        entradas = 0
        saidas = 0

        for t in perfil.transacoes.all():
            if t.tipo == 'saida':
                saldo -= t.valor
                saidas += t.valor
            elif t.tipo == 'entrada':
                saldo += t.valor
                entradas += t.valor


        return render(request, 'tela_principal.html', 
        {'transacoes': transacoes, 'saldo': saldo, 'saidas': saidas, 'entradas': entradas})
    
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
    
def fazer_login(request):
    if request.method == 'GET':
        return render(request, 'tela_login.html')
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')

        user = authenticate(request, username = name, password = password)

        if user is not None:
            login(request, user)
            return redirect('render_create')
        else:
            return HttpResponse(render(request, 'tela_login_erro.html'))
        
def encerrar_login(request):
    logout(request)
    return redirect('login')
            
