from django.shortcuts import render, redirect
from .models import Contatos


def home(request):
    contato = Contatos.objects.all()
    return render(request, "agenda.html", {"contatos": contato})


def registrarcontato(request):
    nome = request.POST['nome']
    telefone = request.POST['telefone']
    email = request.POST['email']
    endereco = request.POST['endereco']
    numero = request.POST['numero']
    cep = request.POST['cep']
    cidade = request.POST['cidade']
    estado = request.POST['estado']


    contato = Contatos.objects.create(nome=nome, telefone=telefone, email=email, endereco=endereco, numero=numero,
                                      cep=cep, cidade=cidade, estado=estado)
    return redirect('/')

def edicaocontato(request, id):
    contato = Contatos.objects.get(id=id)
    return render(request, "edicaocontato.html", {"contatos": contato})

def editarcontato(request):
    id = request.POST['id']
    nome = request.POST['nome']
    telefone = request.POST['telefone']
    email = request.POST['email']
    endereco = request.POST['endereco']
    numero = request.POST['numero']
    cep = request.POST['cep']
    cidade = request.POST['cidade']
    estado = request.POST['estado']

    contato = Contatos.objects.get(id=id)


    contato.nome = nome
    contato.telefone = telefone
    contato.email = email
    contato.endereco = endereco
    contato.numero = numero
    contato.cep = cep
    contato.cidade = cidade
    contato.estado = estado

    contato.save()
    return redirect('/')


def excluircontato(request, id):
    contato = Contatos.objects.get(id=id)
    contato.delete()
    return redirect('/')


def cancelaredicao(request):
    return redirect('/')


