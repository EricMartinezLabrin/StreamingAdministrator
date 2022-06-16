#python
from dateutil.relativedelta import relativedelta

#django
from django import forms
from django.utils import timezone

#local
from .models import Account, AccountName, Sale,Customer



#CREATE
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
#UPDATE
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

#FILTER
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

class FindCustomer(forms.ModelForm):

    class Meta:
        model = Customer
        fields =['email', 'phone']

class SaleForm(forms.ModelForm):

    new_expiration = forms.IntegerField()

    class Meta:
        model = Sale
        fields = ['business',
        'user_seller_id',
        'bank_id',
        'customer_id',
        'account_id',
        'status_id',
        'payment_method_id',
        'payment_amount',
        'invoice']
    
        labels={
            'payment_amount':'Monto de Pago',
            'bank_id': 'N° de Cuenta',
            'payment_method_id': 'Forma de Pago',
            'expiration_date': 'Duración',
            'invoice': 'Comprobante'
        }

        widgets ={
            'user_seller_id': forms.Select(attrs={'class':'form-select'}),
            'payment_amount': forms.NumberInput(attrs={'class': 'form-control','id':'recipient-name'}),
            'payment_method_id': forms.Select(attrs={'class':'form-control'}),
            'expiration_date': forms.DateInput(attrs={'type':'date', 'class':'form-control'}),
            'invoice': forms.TextInput(attrs={'class':'form-control'})
        }
class ChangeSaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields = ['account_id']


class UpdateSaleForm(forms.ModelForm):

    class Meta:
        model = Sale
        fields= ['expiration_date']

        labels={
            'expiration_date': 'Fecha de Vencimiento'
        }

        widgets={
            'expiration_date': forms.DateInput(attrs={'type':'date', 'class':'form-control'})
        }

class NewCustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields= '__all__'

        labels={
            'name': 'Nombre',
            'last_name':'Apellido',
            'email':'E-Mail',
            'phone':'Celular',
            'lada':'Lada',
            'country': 'País',
            'referred_by': 'Recomendado por'
        }

        widgets={
            'name': forms.TextInput(attrs={'class':'form-control','id':'name'}),
            'last_name': forms.TextInput(attrs={'class':'form-control','id':'last_name'}),
            'email': forms.EmailInput(attrs={'class':'form-control','id':'email'}),
            'phone': forms.NumberInput(attrs={'class':'form-control','id':'phone'}),
            'lada': forms.NumberInput(attrs={'class':'form-control','id':'lada'}),
            'country': forms.TextInput(attrs={'class':'form-control','id':'country'}),
            'referred_by': forms.NumberInput(attrs={'class':'form-control','id':'referred_by'})
        }