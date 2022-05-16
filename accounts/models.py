#python


#django
from django.db import models
from django.contrib.auth.models import User
from django.core.validators import RegexValidator


class AccountName(models.Model):
    description = models.CharField(max_length=40)

    def __str__(self):
        return self.description

class Customer(models.Model):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=50)
    email  = models.EmailField(max_length=50, unique=True)
    phone = models.CharField(validators = [phoneNumberRegex],max_length=16, unique=True, null=False, blank=False)
    lada = models.IntegerField()
    country  = models.CharField(max_length=50, null=False)

    def __str__(self):
        return self.name

class Bank(models.Model):
    bank_name = models.CharField(max_length=30, null=False)
    headline = models.CharField(max_length=30, null=False)
    card_number = models.CharField(max_length=16,null=False)
    clabe = models.CharField(max_length=18,null=False)

    def __str__(self):
        return self.card_number

class PaymentMethod(models.Model):
    description = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.description

class Status(models.Model):
    description = models.CharField(max_length=40, null=False)

    def __str__(self):
        return self.description

# class Access(models.Model):
    # description = models.CharField(max_length=30, null=False)


class UserDetail(models.Model):
    phoneNumberRegex = RegexValidator(regex = r"^\+?1?\d{8,15}$")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    phone_number = models.CharField(validators = [phoneNumberRegex],max_length=16,null=False)
    lada = models.IntegerField(null=False)
    country = models.CharField(max_length=40, null=False)

class Account(models.Model):
    status_id = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer, on_delete=models.DO_NOTHING, null=True, blank=True, default="Disponible")
    created_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name = 'created_by')
    modified_by = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='modified_by')
    account_name_id = models.ForeignKey(AccountName, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=True, null=False)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    email = models.EmailField(max_length=50, null=False)
    password = models.CharField(max_length=50, null=False)
    pin = models.IntegerField()
    comments = models.CharField(max_length=250, null=True, blank=True)
    profile = models.IntegerField(null=False)
    sent = models.BooleanField(default=False)

    def __str__(self):
        return self.account_name_id.description

class Sale(models.Model):
    user_seller_id = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    bank_id = models.ForeignKey(Bank,on_delete=models.DO_NOTHING)
    customer_id = models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    account_id = models.ForeignKey(Account,on_delete=models.DO_NOTHING)
    status_id = models.ForeignKey(Status, on_delete=models.DO_NOTHING)
    payment_method_id = models.ForeignKey(PaymentMethod, on_delete=models.DO_NOTHING)
    created_at = models.DateTimeField(auto_now=False, auto_now_add=False)
    expiration_date = models.DateTimeField(auto_now=False, auto_now_add=False, null=False)
    payment_amount = models.IntegerField(null=False)
    invoice = models.CharField(max_length=20, null=False)

    def __str__(self):
        return self.customer_id.phone
