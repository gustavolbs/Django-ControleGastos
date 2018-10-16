from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User
from django.contrib.sites.shortcuts import get_current_site
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.template.loader import render_to_string, get_template
from django.urls import reverse
from django.utils.encoding import force_bytes, force_text
from django.utils.html import strip_tags
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from contas.tokens import account_activation_token
from .models import Transacao
from .form import TransacaoForm, SignUpForm, UserLoginForm
from django.core.mail import send_mail, EmailMessage, EmailMultiAlternatives
from django.conf import settings
from django.template import Context

import datetime, time

# Create your views here.


def home(request):
    data = {}
    data["transacoes"] = Transacao.objects.all()
    data["now"] = datetime.datetime.now()
    return render(request, "contas/home.html", data)


def nova_transacao(request):
    form = TransacaoForm(request.POST or None)
    if form.is_valid():
        #if request.user.is_authenticated:
            if request.user.is_superuser:
                form.save()
                return redirect('url_home')
            else:
                return redirect('url_notSuper')
       # else:
        #    return redirect('url_login')
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
            current_site, uid, token = get_current_site(request), urlsafe_base64_encode(force_bytes(user.pk)).decode(), account_activation_token.make_token(user)
            subject, email_from, to_email = 'Ative sua conta Controller-Gastos', settings.EMAIL_HOST_USER, [form.cleaned_data.get('email')]

            activation_link = "{0}/activate/{1}/{2}".format(current_site, uid, token)
            message = "Hello {0},\n {1}".format(user.username, activation_link)

            html_content = render_to_string('contas/activate.html', {'user': user, 'domain': current_site, 'uidb64': uid, 'token': token, })  # render with dynamic value

            send_mail(subject, message, email_from, to_email, html_message=html_content)
            return HttpResponse('Please confirm your email address to complete the registration')
            # return HttpResponseRedirect('{0}/activate/{1}/{2}/'.format(current_site, uid, token))
            # return render(request, 'contas/activate.html',{'user': user, 'domain': current_site, 'uidb64': uid, 'token': token, })
            # return HttpResponseRedirect(request, )

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
        HttpResponse('Account activated successfully')
        time.sleep(5)
        return redirect('url_home')
    else:
        return render(request, 'contas/account_activation_invalid.html')


def login(request):
    title = "Login"
    form = UserLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        user = authenticate(username=username,password=password)
        login(request, user)
        return redirect('url_home')
    return render(request, 'contas/login.html', {'form':form, 'title':title})


def notSuper(request):
    return render(request, 'contas/notSuper.html')

def activation_sent(request):
    return render(request, 'contas/activation_sent.html')