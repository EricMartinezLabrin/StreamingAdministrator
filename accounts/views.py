#django
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.urls import reverse

#local
from .models import Account


## Login - Logour
class LoginFormView(LoginView):
    template_name= 'accounts/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context

class LogoutFormView(LogoutView):
    pass

# Admin Views
class DashboardView(generic.TemplateView):
    model = User
    template_name = 'accounts/dashboard.html'

class ActiveAccountView(generic.ListView):
    model = Account
    template_name = 'accounts/active_accounts.html'
    context_object_name = "active_accounts"

    def get_queryset(self):
        """
        Show all data accounts with status active
        """
        return Account.objects.filter(status_id=1)