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
    path("sales/redeem/find", login_required(views.FindCuponFunc),name="find_cupon"),
    path("sales/redeem/<int:pk>", login_required(views.RedeemFunc),name="redeem"),
    path("sales/renew/<int:pk>/", login_required(views.RenewSale), name="renew_sale"),
    path("sales/update/<int:pk>/", login_required(views.UpdateSale), name="update_sale"),
    path("sales/update/change_sale/<int:pk>/", login_required(views.ChangeSaleFunc), name="change_sale"),
    path("sales/create/<int:pk>", login_required(views.NewSaleFunc), name='create'),
    path("customer/create/", login_required(views.NewCustomerFunc), name='new_customer'),
    path("release/<int:pk>/<int:user>/", login_required(views.ReleaseAccountFunc), name='release')
    ]