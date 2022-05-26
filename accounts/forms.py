from django import forms
from .models import Account, AccountName
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
            'expiration_date': forms.TextInput(attrs={'type':'date','class':'form-control'}),
            'email': forms.EmailInput(attrs={'class':'form-control'}),
            'password': forms.TextInput(attrs={'type': 'password','class':'form-control'}),
            'comments': forms.TextInput(attrs={'class':'form-control'}),
            'account_name_id': forms.Select(attrs={'class':'form-control'}),
            'supplier': forms.Select(attrs={'class':'form-control'}),
            'renovable': forms.CheckboxInput(attrs={'id':'renovable'}),
            'pin': forms.NumberInput(attrs={'class':'form-control','id':'pin'})

        }

class FilterAccountForm(forms.ModelForm):

    class Meta:
        model = Account

        fields = ['account_name_id','email','status_id']
        labels = {
            'account_name_id': 'Cuenta',
            'email': 'E-Mail',
            'status_id': 'Estado'

        }
        widgets = {
            'account_name_id': forms.Select(attrs={'class':'form-select','id':'inputGroupSelect01'}),
            'email': forms.TextInput(attrs={'id':'addon-wrapping','value':'---------'}),
            'status_id': forms.Select(attrs={'class':'form-select','id':'status'})
        }

class EditAccountForm(forms.ModelForm):
    
    class Meta:
        model = Account
        fields = ['account_name_id','expiration_date','email','password','pin','supplier','comments','renovable','modified_by']
        labels = {
            'supplier': 'Proveedor',
            'expiration_date': 'Fecha de Vencimiento',
            'email': "E-Mail",
            'password': "Password",
            'pin': 'Pin',
            'comments': "Comentarios",
            'account_name_id': 'Cuenta',
            'renovable': 'Es Renovable'
        }
        widgets={
            'comments': forms.TextInput(attrs={'class':'form-control','id':'comments'}),
            'password': forms.TextInput(attrs={'class':'form-control','id':'password'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'pin': forms.NumberInput(attrs={'class':'form-control','id':'pin'}),
            'expiration_date': forms.DateInput(attrs={'type':'date','class':'form-control','id':'expiration_date'}),
            'account_name_id': forms.Select(attrs={'class':'form-control','id':'account_name_id'}),
            'supplier': forms.Select(attrs={'class':'form-control','id':'supplier'}),
            'renovable': forms.CheckboxInput(attrs={'id':'renovable'})
            
        }

