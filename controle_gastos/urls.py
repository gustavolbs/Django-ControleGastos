"""controle_gastos URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from contas.views import home, nova_transacao, update, delete, notSuper, signUp, activation_sent, activate, login

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='url_home'),
    path('update/<int:pk>/', update, name='url_update'),
    path('delete/<int:pk>/', delete, name='url_delete'),
    path('403/', notSuper, name='url_notSuper'),
    path('form/', nova_transacao, name='url_novaTransacao'),
    path('signup/', signUp, name='url_signUp'),
    path('login/', login, name='url_login'),
    path('signup/activation_sent/', activation_sent, name='url_activationSent'),
    path('activate/<slug:uidb64>/<slug:token>/', activate, name='activate'),

]
