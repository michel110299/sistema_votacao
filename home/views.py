from django.shortcuts import render 
from cadastro.models import Votacao
from django.utils import timezone


def index(request):
    objVotacoes = Votacao.objects.filter(horario_termino__gt=timezone.now())

    context = {
        "listVotacoes": objVotacoes,
        "nome_pagina": "Votações ativas",
    }

    return render(request, "index.html", context)
