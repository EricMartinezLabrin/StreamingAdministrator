#python
from datetime import timedelta
import requests

#django
from django.test import TestCase, SimpleTestCase
from django.urls import reverse
from django.utils import timezone


#local
from .models import Account, Status, Sale
from .views import NewSaleFunc


#Functions to add data to database

# class SaleFormView(TestCase):

#     def check_if_is_valid_form(self):
#         data{
#             'business': 1
#             'user_seller_id': 1
#             'bank_id': 1
#             'customer_id': 1
#             'account_id': 1
#             'status_id': 1
#             'payment_method_id': 1
#             'created_at': timezone.now()
#             'expiration_date': timezone.now()+timedelta(month=1)
#             'payment_amount': 85
#             'invoice': 'fdsfdsfds'
#         }

#     resp = requests.post(reverse())
