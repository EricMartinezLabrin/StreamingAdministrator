#django
from django.shortcuts import render
from django.views import generic
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.views import LoginView

#local
from .models import AccountName

class LoginFormView(LoginView):
    template_name= 'accounts/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context