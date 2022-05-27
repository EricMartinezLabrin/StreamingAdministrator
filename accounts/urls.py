#django
from django.urls import path
from django.contrib.auth.decorators import login_required

from . import views

app_name = "accounts"
urlpatterns = [
    #extension: /accounts/
    path("", views.LoginFormView.as_view(redirect_authenticated_user=True), name ="index"),
    path("dashboard/", login_required(views.DashboardView.as_view()), name ="dashboard"),
    path("logout/", views.LogoutFormView.as_view(), name="logout"),
    path("list_account/", login_required(views.ActiveAccountFunc),name="list_account"),
    path("list_account/create/", login_required(views.CreateAccounts), name="create_account"),
    path("list_account/edit/<int:pk>/", login_required(views.EditAccountView.as_view()), name="edit"),
    path("list_account/edit/layoff_layon/<str:account_name_id>/<str:email>/<int:status>", login_required(views.LayoffLayonAccountFunc), name="layoff_layon"),
    path("list_account/detail/<int:pk>/", login_required(views.DetailAccountFunc), name="detail"),
    path("sales/", login_required(views.SaleFunc),name="sales"),
    ]