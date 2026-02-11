from django.urls import path
from dindintrack import views

urlpatterns = [
    path('controle/', views.ControleFinanceiro.as_view(), name='render_create')
]