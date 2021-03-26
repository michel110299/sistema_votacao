from django.urls import path
from .import views

urlpatterns = [
    path('registrar-pessoa/', views.registrar_pessoa, name="registrar_pessoa"),
    path('registrar-votacao/', views.registrar_votacao, name="registrar_votacao"),
    path('registrar-opcao-voto/', views.registrar_opcao_voto,name="registrar_opcao_voto"),
    path("votacao/<int:id>",views.informacoes_votacao, name= "informacoes_votacao"),
]