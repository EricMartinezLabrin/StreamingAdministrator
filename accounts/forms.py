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
            'expiration_date': forms.TextInput(attrs={'type':'date'}),
            'email': forms.EmailInput(),
            'password': forms.TextInput(attrs={'type': 'password'}),
            'comments': forms.Textarea(),
            'account_name_id': forms.Select(),
            'supplier': forms.Select()
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
        fields = ['account_name_id','expiration_date','email','password','pin','supplier','comments']
        labels = {
            'supplier': 'Proveedor',
            'expiration_date': 'Fecha de Vencimiento',
            'email': "E-Mail",
            'password': "Password",
            'pin': 'Pin',
            'comments': "Comentarios",
            'account_name_id': 'Cuenta'
        }
        widgets={
            'comments': forms.Textarea(),
            'email': forms.EmailInput(),
            'expiration_date': forms.DateInput(attrs={'type':'date'})
        }

# class InactiveButtonForm(forms.ModelForm):

#     class Meta:
#         model = Account
#         field = ['status_id']