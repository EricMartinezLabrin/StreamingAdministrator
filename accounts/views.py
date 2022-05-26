from django.forms import DateTimeInput, TextInput, Widget
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.models import User
from django.views.generic.edit import UpdateView
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import permission_required
from django.contrib import messages



#local
from .models import Account,AccountName,UserDetail,Status, Sale
from .forms import CreateAccountForm, FilterAccountForm, EditAccountForm
from .functions import SearchExistent



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
    # account.status_id= status
    # account.save()
    messages.success(request, layoff_message)
    return HttpResponseRedirect(reverse('accounts:list_account',))


def DetailAccountFunc(request, pk):
    
    detail = Sale.objects.filter(account_id = pk)

    return render(request,'accounts/detail.html', {
        'detail':detail
    })