#django
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "accounts"
urlpatterns = [
    #extension: /accounts/
    path("", views.LoginFormView.as_view(redirect_authenticated_user=True), name ="index"),
    path("dashboard", login_required(views.DashboardView.as_view()), name ="dashboard"),
    path("logout", views.LogoutFormView.as_view(), name="logout"),
    path("list_account", login_required(views.ActiveAccountView.as_view()),name="list_account")

    ]