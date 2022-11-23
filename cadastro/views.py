from django.shortcuts import render, redirect
from django.http import HttpResponse

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
        return render(request, "register_user.html", {'sorte':pessoas})
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
        return redirect('/')