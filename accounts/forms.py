from django import forms
from .models import Account
from django.utils import timezone

class CreateAccountForm(forms.ModelForm):

    class Meta:
        model = Account

        fields = '__all__'
        labels = {
            'expiration_date': 'Fecha de Vencimiento',
            'email': 'E-Mail',
            'password': 'Password',
            'pin': 'Pin',
            'comments': 'Comentarios',
            'account_name_id': 'Cuenta',
            'supplier': 'Proveedor'
        }
        widgets = {
            'expiration_date': forms.TextInput(attrs={'type':'date'}),
            'email': forms.TextInput(attrs={'type': 'email'}),
            'password': forms.TextInput(attrs={'type': 'password'}),
            'comments': forms.Textarea(),
            'account_name_id': forms.Select(),
            'supplier': forms.Select()
        }