from django.contrib import admin
from .models import AccountName, Customer, Bank, PaymentMethod, Status, UserDetail, Account, Sale

# Register your models here.
admin.site.register(AccountName)
admin.site.register(Customer)
admin.site.register(Bank)
admin.site.register(PaymentMethod)
admin.site.register(Status)
admin.site.register(UserDetail)
admin.site.register(Account)
admin.site.register(Sale)
    