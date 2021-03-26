from django.urls import path
from .import views

urlpatterns = [
    path('iniciar-votacao/<int:id>', views.iniciar_votacao, name="iniciar_votacao"),
    path('validacao-pessoa/<int:id>', views.validacao_pessoa, name="validacao_pessoa"),
]