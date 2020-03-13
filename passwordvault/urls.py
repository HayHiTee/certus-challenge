from django.urls import path
from django.conf.urls import include
from . import views

urlpatterns = [
	path("pv/", views.PasswordVaultView.as_view(), name="password-vault"),
	]