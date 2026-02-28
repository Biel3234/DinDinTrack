from django.urls import path
from dindintrack import views

urlpatterns = [
    path('controle/', views.ControleFinanceiro.as_view(), name='render_create'),
    path('login/', views.fazer_login, name='login' ),
    path('logout/', views.encerrar_login, name='deslogar'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro'),
    path('deletar_transacao/<int:pk>', views.deletar_transacao, name='deletar'),
    path('editar/<int:pk>', views.editar_transacao, name='editar'),
    path('cartao/', views.Adcionar_cartao.as_view(), name='criar_cartao')
]