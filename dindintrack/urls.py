from django.urls import path
from dindintrack import views

urlpatterns = [
    path('controle/', views.ControleFinanceiro.as_view(), name='render_create'),
    path('login/', views.fazer_login, name='login' ),
    path('logout/', views.encerrar_login, name='deslogar'),
    path('cadastro/', views.cadastrar_usuario, name='cadastro')
]