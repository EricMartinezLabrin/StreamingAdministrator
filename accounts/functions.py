#django
from django.shortcuts import get_object_or_404

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


