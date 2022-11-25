from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.template import loader
from .models import Cadastro

# Create your views here.
def menu(request):
    return render(request, "menu.html")

def check_user(request):
    pessoas = Cadastro.objects.all()
    return render(request, "check_user.html", {'pessoas':pessoas})

def register_user(request):
    if request.method == "GET":
        pessoas = Cadastro.objects.all()
        return render(request, "register_user.html", {'pessoas':pessoas})
    elif request.method == "POST":
        firstName = request.POST.get('firstName')
        lastName = request.POST.get('firstName')
        cpf = request.POST.get('cpf')
        email = request.POST.get('email')
        age = request.POST.get('age')
    
        pessoas = Cadastro(
            firstName=firstName,
            lastName=lastName,
            cpf=cpf,
            email=email,
            age=age
        )
        pessoas.save()
        return redirect('check_user/')

# vizualização do update
def update_user(request):
    pessoas = Cadastro.objects.all()
    return render(request, "update_user.html", {'pessoas': pessoas})

# update
def update(request, id):
    pessoas = Cadastro.objects.get(id=id)
    print(f' Pessoa escolhida pelo id para fazer update{pessoas}')
    return render(request, "update.html", {'pessoas': {pessoas}} )
def update_record(request, id):
    pessoas = Cadastro.objects.get(id=id)
    template = loader.get_templates('update_record.html')
    context = {
        'pessoas': pessoas,
    }
    return HttpResponse(template(context,request))

def delete(request, id):
    pessoa = Cadastro.objects.get(id=id)
    pessoa.delete()
    print(f'Voce excluiu {pessoa}')
    return HttpResponseRedirect(reverse('update_user'))