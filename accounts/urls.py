#django
from django.urls import path
from django.contrib.auth import login, logout

from . import views

app_name = "accounts"
urlpatterns = [
    #extension: /accounts/
    path("", views.LoginFormView.as_view(), name ="index"),

    ]