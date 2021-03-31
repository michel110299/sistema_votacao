from django.shortcuts import render 
from cadastro.models import Votacao
from django.utils import timezone


def index(request):
    #objVotacoes_ativas = Votacao.objects.filter(horario_inicio__lt=timezone.now(),horario_termino__gt=timezone.now())
    objVotacoes = Votacao.objects.all()

    data_atual = timezone.now()
    context = {
        "listVotacoes": objVotacoes,
        "nome_pagina": "Todas votações",
        "data_atual":data_atual
    }

    return render(request, "index.html", context)
