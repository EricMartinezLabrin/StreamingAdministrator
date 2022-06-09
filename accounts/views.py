#python
import datetime
from http.client import NOT_FOUND
from platform import release
from xml.dom import NotFoundErr
from dateutil.relativedelta import relativedelta

#django
from django.forms import DateTimeInput, TextInput, Widget
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic.edit import CreateView, UpdateView
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages
from django.utils import timezone



#local
from .models import Account,AccountName,UserDetail,Status,Sale,Customer
from .forms import CreateAccountForm, FilterAccountForm, EditAccountForm, SaleForm
from .functions import SearchExistent, UpdateAccount


## Login - Logour
class LoginFormView(LoginView):
    """
    Show Login page
    """
    template_name= 'accounts/index.html'
    model = User

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Iniciar Sesión'
        return context

class LogoutFormView(LogoutView):
    """
    Logout user
    """
    pass

# Admin Views
class DashboardView(generic.TemplateView):
    """
    Show all data of template
    """
    model = User
    template_name = 'accounts/dashboard.html'

@permission_required('accounts.view_account', raise_exception=True)
def ActiveAccountFunc(request):
    """
    Show all active accounts filtered by Bussiness ID of person are looking for And Pagintate by 10
    """
    business_id = request.user.userdetail.business

    form = FilterAccountForm()
    if request.method == 'POST':
        account_name_id=request.POST['account_name_id']
        email = request.POST['email']
        status_id = request.POST['status_id']
        if email == '---------':
            accounts = Account.objects.filter(
            business_id= business_id,
            account_name_id=account_name_id,
            status_id=status_id
            )
        else:
            accounts = Account.objects.filter(
                business_id= business_id,
                account_name_id=account_name_id,
                email=email,
                status_id=status_id
                )
            #Set Up Pagination
        p =Paginator(accounts, 10)
        page = request.GET.get('page')
        venues = p.get_page(page)
        return render(request, "accounts/active_accounts.html",{
            "accounts": accounts,
            "venues": venues,
            "form": form
        })
    else:
        active = 1
        accounts = Account.objects.filter(status_id=active, business_id= business_id)
            #Set Up Pagination
        p =Paginator(accounts, 10)
        page = request.GET.get('page')
        venues = p.get_page(page)
        return render(request, "accounts/active_accounts.html",{
            "accounts": accounts,
            "venues": venues,
            "form": form
        })

def CreateAccounts(request):
    """
    Add new account to actual bussines are loged in
    """
    if request.method == 'POST':
        form = CreateAccountForm(request.POST)
        user_details = UserDetail
        account = request.POST['account_name_id']
        perfil = AccountName.objects.get(pk=account)
        perfil = perfil.perfil_quantity
        
        if form.is_valid():
            for new_profile in range(1,perfil+1):
                account_name_id = form.cleaned_data['account_name_id']
                supplier = form.cleaned_data['supplier']
                expiration_date = form.cleaned_data['expiration_date']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                pin = form.cleaned_data['pin']
                comments = form.cleaned_data['comments']
                business = form.cleaned_data['business']
                created_by = form.cleaned_data['created_by']
                modified_by = form.cleaned_data['modified_by']
                exist = SearchExistent.search_by_email_account_id(
                    models=Account,
                    account_id=account_name_id,
                    email=email,
                    profile=new_profile
                    )
                if exist == False:
                    Account.objects.create(
                        account_name_id=account_name_id,
                        supplier=supplier,
                        expiration_date=expiration_date,
                        email=email,
                        password=password,
                        pin=pin,
                        comments=comments,
                        business=business,
                        created_by=created_by,
                        modified_by=modified_by,
                        profile=new_profile
                        )
                else:
                    return render(request, 'accounts/create_account.html',{
                        'form': form,
                        'error_message': f"El {account_name_id} con E-Mail {email} ya fue utilizado. Porfavor intenta con uno nuevo."
                    })
        else:
            raise Exception("Formulario No Valido")
        return redirect('accounts:list_account')
    else: 
        form = CreateAccountForm()
    return render(request, 'accounts/create_account.html', {
        'form': form,
    }
        )

class EditAccountView(UpdateView):
    model = Account
    form_class = EditAccountForm
    template_name = 'accounts/update_accounts.html'
    success_url = reverse_lazy('accounts:list_account')
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

def DetailAccountFunc(request, pk):
    
    detail = Sale.objects.filter(account_id = pk)

    return render(request,'accounts/detail.html', {
        'detail':detail
    })

def SaleFunc(request,customer=None):
    available_accounts = SearchExistent.get_available_accounts(request)
    try:
        if customer == None:
            customer = request.POST["customer"]
        else:
            customer = customer

        is_email = False
        is_phone = False
        # now = datetime.now()
        #check if data is email or phone number
        if customer.isnumeric():
            is_phone = True
        else:
            is_email = True
    
            #get customer_id
        if is_email == True:
            customer_id = Customer.objects.get(email__contains=customer)
        if is_phone == True:
            customer_id = Customer.objects.get(phone__contains= customer)
        
        #Dactivate all accoutns with expiration date <= today
        UpdateAccount.deactivate_due(Sale,customer_id.id)
        #find all active accounts
        active_sales = Sale.objects.filter(customer_id=customer_id.id,status_id='1')
        #find all inactive accounts
        inactive_sales = Sale.objects.filter(customer_id=customer_id.id,status_id='2')
        return render(request,'accounts/sales.html',{
            'active_sales':active_sales,
            'inactive_sales':inactive_sales,
            'customer': customer_id,
            'available_accounts': available_accounts,
            'available_accounts_count': available_accounts
            })
            
    except:
        return render(request, "accounts/sales.html",{
            "error_message": "El cliente no existe, verifica que no tenga el codigo de pais"
        })

def RenewSale(request,pk):
    sale = Sale.objects.get(pk=pk)
    form = SaleForm(request.POST or None, instance=sale)

    if request.method == 'POST':
        if form.is_valid():
            #find all values
            new_expiration = int(form.data['new_expiration'])
            business = form.cleaned_data['business']
            user_seller_id = form.cleaned_data['user_seller_id']
            bank_id = form.cleaned_data['bank_id']
            customer_id = form.cleaned_data['customer_id']
            account_id = form.cleaned_data['account_id']
            status_id = form.cleaned_data['status_id']
            payment_method_id = form.cleaned_data['payment_method_id']
            created_at = timezone.now()
            expiration_date = sale.expiration_date+relativedelta(months=new_expiration)
            payment_amount = form.cleaned_data['payment_amount']
            invoice = form.cleaned_data['invoice']
            #Search if invoice has used
            try:
                invoice_exist = get_object_or_404(Sale,invoice=invoice)
                return HttpResponse("<h2>El comprobante ya fue utilizado</h2>")
            except(Sale.MultipleObjectsReturned):
                return HttpResponse("<h2>El comprobante ya fue utilizado</h2>")
            except (Sale.DoesNotExist,Http404):
                #Deactivate Old Sale
                Sale.objects.filter(pk=pk).update(status_id=2)

                # create new sale
                Sale.objects.create(
                    business=business,
                    user_seller_id=user_seller_id,
                    bank_id=bank_id,
                    customer_id=customer_id,
                    account_id=account_id,
                    status_id=status_id,
                    payment_method_id=payment_method_id,
                    expiration_date=expiration_date,
                    created_at=created_at,
                    payment_amount=payment_amount,
                    invoice=invoice
                    )

                # Update Expiration date
                Sale.objects.filter(invoice=invoice).update(expiration_date=expiration_date)
            #Dactivate all accoutns with expiration date <= today
            UpdateAccount.deactivate_due(Sale,customer_id)
            active_sales = Sale.objects.filter(customer_id=customer_id,status_id='1')
            inactive_sales = Sale.objects.filter(customer_id=customer_id,status_id='2')
            return render(request,'accounts/sales.html',{
                'active_sales':active_sales,
                'inactive_sales':inactive_sales,
                'customer': customer_id
                })
        return HttpResponse(form)
    else:
        return render(request,'accounts/renew_sale.html',{
            'form':form,
            'sale':sale,
            'customer':sale.customer_id
        })

def NewSaleFunc(request, pk):
    business_id = request.user.userdetail.business
    form = SaleForm
    account_name = AccountName.objects.all()
    all_account = Account.objects.all()
    disponible_accounts = Account.objects.filter(customer_id=None, expiration_date__gt=timezone.now(), business_id=business_id).order_by('expiration_date','profile')
    sales = Sale.objects.filter(business_id=business_id,status_id=1)
    

    if request.method=='POST':
        form = SaleForm(request.POST)
        if form.is_valid():
            #find all values
            new_expiration = int(form.data['new_expiration'])
            business = form.cleaned_data['business']
            user_seller_id = form.cleaned_data['user_seller_id']
            bank_id = form.cleaned_data['bank_id']
            customer_id = form.cleaned_data['customer_id']
            account_id = form.cleaned_data['account_id']
            status_id = form.cleaned_data['status_id']
            payment_method_id = form.cleaned_data['payment_method_id']
            created_at = timezone.now()
            expiration_date = timezone.now() + relativedelta(months=new_expiration)
            payment_amount = form.cleaned_data['payment_amount']
            invoice = form.cleaned_data['invoice']
            try:
                invoice_exist = get_object_or_404(Sale,invoice=invoice)
                return HttpResponse("<h2>El comprobante ya fue utilizado</h2>")
            except(Sale.MultipleObjectsReturned):
                return HttpResponse("<h2>El comprobante ya fue utilizado</h2>")
            except (Sale.DoesNotExist,Http404):
                #create new sale
                Sale.objects.create(
                    business=business,
                    user_seller_id=user_seller_id,
                    bank_id=bank_id,
                    customer_id=customer_id,
                    account_id=account_id,
                    status_id=status_id,
                    payment_method_id=payment_method_id,
                    created_at=created_at,
                    expiration_date=expiration_date,
                    payment_amount=payment_amount,
                    invoice=invoice
                    )
                
                # Put account as Sold
                Account.objects.filter(pk=account_id.id).update(customer_id=customer_id.id,modified_by=user_seller_id)
                # Update Expiration date
                Sale.objects.filter(invoice=invoice).update(expiration_date=expiration_date)
                #find all active accounts
                active_sales = Sale.objects.filter(customer_id=customer_id,status_id='1')
                #find all inactive accounts
                inactive_sales = Sale.objects.filter(customer_id=customer_id,status_id='2')
                return render(request,'accounts/sales.html',{
                    'active_sales':active_sales,
                    'inactive_sales':inactive_sales,
                    'customer': customer_id
                    })
        return HttpResponse("<h1>Hay un error en la información</h1><p>Porfavor corroborelo y vuelva a intentar</p>")

    else:
        return render(request,'accounts/new_sale.html',{
            'form':form,
            'customer_id': pk,
            'account_name':account_name,
            'disponible_accounts':disponible_accounts,
            'all_account':all_account,
            'sales': sales
        })


#Buttons
def LayoffLayonAccountFunc(request,account_name_id,email,status):
    """
    It View Suspend an active account if status = 1 or Reactive an inactive account if status = 2
    """
    account = Account.objects.filter(account_name_id=account_name_id,email=email)
    if status == 1:
        status = Status.objects.get(description='inactive')
        layoff_message= f"La cuenta email {email} fue suspendida Correctamente"

    else:
        status = Status.objects.get(description='active')
        layoff_message= f"La cuenta email {email} fue Reactivada Correctamente"

    
    for layoff in account:
        layoff.status_id=status
        layoff.save()
    messages.success(request, layoff_message)
    return HttpResponseRedirect(reverse('accounts:list_account',))

def ReleaseAccountFunc(request, pk, user):
    """
    Release account and put it Available to sell again
    """
    #get data
    sale = Sale.objects.get(pk=pk)

    #suspend sale
    Sale.objects.filter(pk=pk).update(status_id=2)

    account_id = sale.account_id.id

    # release account
    release = Account.objects.filter(pk=account_id).update(customer_id=None,modified_by=user)

    #success message
    release_message= "La cuenta fue liberada correctamente"
    messages.success(request, release_message)
    #find all active accounts
    active_sales = Sale.objects.filter(customer_id=sale.customer_id.id,status_id='1')
    #find all inactive accounts
    inactive_sales = Sale.objects.filter(customer_id=sale.customer_id.id,status_id='2')
    return render(request,'accounts/sales.html',{
        'active_sales':active_sales,
        'inactive_sales':inactive_sales,
        'customer': sale.customer_id
        })
