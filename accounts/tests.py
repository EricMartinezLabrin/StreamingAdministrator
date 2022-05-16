#python
from datetime import timedelta

#django
from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

#local
from .models import Account, Status


#Functions to add data to database

def create_status():
    active = Status.objects.create(description = 'active')
    inactive = Status.object.create(description = 'inactive')

    return active, inactive

def create_account(
    status_id = 1, 
    customer_id = 1, 
    created_by = 1, 
    modified_by = 1, 
    account_name_id=1, 
    created_at=timezone.now(), 
    expiration_date=timezone.now + timedelta(days=30), 
    email="pruebas@puebas.com",
    password="pruebas",
    pin= 1234,
    comments="",
    profile=1,
    sent=False
    )

    return Account.objects.create(
        status_id=status_id, 
        customer_id=customer_id,
        created_by=created_by,
        modified_by=modified_by,
        account_name_id=account_name_id,
        created_at=created_at,
        expiration_date=expiration_date,
        email=email,
        password=password,
        pin=pin,
        comments=comments,
        profile=profile,
        sent=sent
        )


class AccountsActiveAccountsView(TestCase):

    def test_show_only_active_accounts(self):
        """
        Show True if a inactive account is detected
        """
        create_status()
        add_account_active = create_account(status_id=1)
        add_account_inactive = create_account(status_id=2)
        url = Account.obtects.filter(status_id=1)