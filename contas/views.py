from django.shortcuts import render, redirect
from .models import Transacao
from .form import TransacaoForm

import datetime

# Create your views here.

def home(request):
    data = {}
    data["transacoes"] = Transacao.objects.all()
    data["now"] = datetime.datetime.now()
    return render(request, "contas/home.html", data)

def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid() and request.user.is_superuser():
        form.save()
        return redirect('url_home')
    return render(request, "contas/form.html", {"form": form})

def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid() and request.user.is_superuser():
        form.save()
        return redirect('url_home')
    return render(request, "contas/form.html", {"form": form, "transacao": transacao})

def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    if request.user.is_superuser():
    	transacao.delete()
    	return redirect('url_home')
	return redirect('url_home')
    
