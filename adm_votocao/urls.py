from django.urls import path
from .import views

urlpatterns = [
    path('iniciar-votacao/<int:id_votacao>/<int:id_pessoa>', views.iniciar_votacao, name="iniciar_votacao"),
    path('validacao-pessoa/<int:id_votacao>', views.validacao_pessoa, name="validacao_pessoa"),
    path('apuracao-votos/<int:id_votacao>', views.apuracao_votos, name="apuracao_votos"),
]