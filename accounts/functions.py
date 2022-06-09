#django
from django.shortcuts import get_object_or_404
from django.utils import timezone
#local
from .models import AccountName, Account

class SearchExistent():


    def search_by_email_account_id(models,account_id,email,profile):
        """
        It function search a email in data base, where mode is db table and email to find.

        Returns True if exist or False is does not Exist
        """
        finder = models.objects.filter(account_name_id=account_id,email=email,profile=profile).count()
        if finder > 0:
            return True
        elif finder == 0:
            return False
        else:
            raise('Existe un error con esta cuenta, porfavor verificar')

    def get_available_accounts(request):
        business_id = request.user.userdetail.business
        now = timezone.now()
        account_names = AccountName.objects.all()
        available_accounts = []
        for name in account_names:
            q = Account.objects.filter(business_id=business_id,account_name_id=name,status_id=1,customer_id=None,expiration_date__gte=now).count()
            available_accounts.append(name.description + ": " + str(q) + " ")
        return available_accounts



class UpdateAccount():

    def deactivate_due(model,customer_id):
        """
        Deactive all expired accounts
        """
        try:
            return model.objects.filter(customer_id=customer_id, expiration_date__lte=timezone.now()).update(status_id=2)
        except:
            return False