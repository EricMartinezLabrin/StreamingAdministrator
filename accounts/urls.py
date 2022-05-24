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
    path("list_account/edit/<int:pk>/", login_required(views.EditAccounFunc), name="edit"),
    path("list_account/edit/layoff/<str:account_name_id>/<str:email>/", login_required(views.LayoffAccountFunc), name="layoff"),
    path("list_account/detail/<int:pk>/", login_required(views.DetailAccountFunc), name="detail")
    ]