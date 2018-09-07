from django.contrib.auth import login
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from contas.tokens import account_activation_token
from .models import Transacao
from .form import TransacaoForm, SignUpForm
from django.core.mail import send_mail
from django.conf import settings

import datetime

# Create your views here.


def home(request):
    data = {}
    data["transacoes"] = Transacao.objects.all()
    data["now"] = datetime.datetime.now()
    return render(request, "contas/home.html", data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        if request.user.is_authenticated:
            if request.user.is_superuser:
                form.save()
                return redirect('url_home')
            else:
                return redirect('url_notSuper')
        else:
            return redirect('url_login')
    return render(request, "contas/form.html", {"form": form})


def update(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    form = TransacaoForm(request.POST or None, instance=transacao)
    if form.is_valid():
        if request.user.is_authenticated:
            if request.user.is_staff:
                form.save()
                return redirect('url_home')
            else:
                return redirect('url_notSuper')
        else:
            return redirect('url_login')
    return render(request, "contas/form.html", {"form": form, "transacao": transacao})


def delete(request, pk):
    transacao = Transacao.objects.get(pk=pk)
    if request.user.is_authenticated:
        if request.user.is_staff:
            transacao.delete()
            return redirect('url_home')
        else:
            return redirect('url_notSuper')
    else:
        return redirect('url_login')


def signUp(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST or None)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()
            current_site = get_current_site(request)
            subject = 'Ative sua conta Controller-Gastos'
            uid = urlsafe_base64_encode(force_bytes(user.pk))
            token = account_activation_token.make_token(user)
            activation_link = "{0}/?uid={1}&token{2}".format(current_site, uid, token)
            email_from = settings.EMAIL_HOST_USER
            # user_email = [user.email]
            to_email = [form.cleaned_data.get('email')]
            message = "Hello {0},\n {1}".format(user.username, activation_link)
            send_mail(subject, message, email_from, to_email)
            return HttpResponse('Please confirm your email address to complete the registration')
    else:
        form = SignUpForm()
    return render(request, 'contas/signUp.html', {'form': form})


def activate(request, uidb64, token):
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except (TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None

    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.profile.email_confirmed = True
        user.save()
        login(request, user)
        return redirect('url_home')
    else:
        return render(request, 'contas/account_activation_invalid.html')



def notSuper(request):
    return render(request, 'contas/notSuper.html')

def activation_sent(request):
    return render(request, 'contas/activation_sent.html')