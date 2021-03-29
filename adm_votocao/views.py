from django.shortcuts import render,redirect
from cadastro.models import *
from django.contrib import messages
from adm_votocao.models import Pessoa_voto


def apuracao_votos(request,id_votacao):


    votacao = Votacao.objects.get(pk=id_votacao)

    todas_votacoes = Pessoa_voto.objects.filter(votacao=votacao)

    context = {
        "todas_votacoes":todas_votacoes,
        "nome_pagina": votacao,
        "votacao":votacao,
    }



    return render(request,"apuracao_votos.html",context)

def validacao_pessoa (request,id_votacao):
    

    if request.POST:
        
        cpf_validacao = request.POST.get('cpf', None)

        try:
            objpessoa = Pessoa.objects.get(cpf=cpf_validacao)
            id_pessoa = objpessoa.id

            return redirect("iniciar_votacao",id_votacao,id_pessoa) 
            
        except Pessoa.DoesNotExist:
        
            messages.error(request,"Não temos esse cpf cadastrado!")
    
    context = {
    "nome_pagina":"Validação do CPF"
    }


    return render(request,"validacao_pessoa.html",context)



def iniciar_votacao(request,id_votacao,id_pessoa):


    objVotacao = Votacao.objects.get(pk=id_votacao)
    objPessoa = Pessoa.objects.get(pk=id_pessoa)

    if  Pessoa_voto.objects.filter(pessoa=objPessoa,votacao=objVotacao) and objVotacao.voto_unico == True:
        messages.error(request,"O voto é unico!")
        return redirect("index") 



    listOpcaoVoto = Opcao_voto.objects.filter(votacao=objVotacao)


    
    if request.POST:
        idOpcaoVoto = request.POST.get('voto', None)
        objOpcaoVoto = Opcao_voto.objects.get(pk=idOpcaoVoto)
        objOpcaoVoto.quantidade_votos += 1
        objOpcaoVoto.save()

       

        try:
            objPessoa_voto = Pessoa_voto.objects.get(pessoa=objPessoa,votacao=objVotacao,opcao_voto=objOpcaoVoto)
            objPessoa_voto.quantidade_votos += 1
            

        except:
            objPessoa_voto = Pessoa_voto()
            objPessoa_voto.pessoa = objPessoa    
            objPessoa_voto.votacao = objVotacao
            objPessoa_voto.opcao_voto = objOpcaoVoto
            objPessoa_voto.quantidade_votos += 1
        
        
        objPessoa_voto.save()


        return redirect('apuracao_votos',id_votacao)



    context = {
        "objVotacao": objVotacao,
        "listOpcaoVoto": listOpcaoVoto,
        "nome_pagina":"Votação"
    }
    

    return render(request, "iniciar_votacao.html", context)







