from django.shortcuts import render,redirect
from cadastro.models import *



def validacao_pessoa (request,id):
    
    todas_pessoas = Pessoa.objects.all()

    if request.POST:
        
        for x in todas_pessoas:

            if x.cpf == request.POST.get('cpf', None):
                
                return redirect("iniciar_votacao",id)


    return render(request, "validacao_pessoa.html")



def iniciar_votacao(request,id):

    objVotacao = Votacao.objects.get(pk=id)

    listOpcaoVoto = Opcao_voto.objects.filter(votacao=objVotacao)
    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = Opcao_voto.objects.get(pk=idOpcaoVoto)

        objOpcaoVoto.quantidade_votos += 1
        objOpcaoVoto.save()
        return redirect('index')

    context = {
        "objVotacao": objVotacao,
        "listOpcaoVoto": listOpcaoVoto,
    }

    return render(request, "iniciar_votacao.html", context)







