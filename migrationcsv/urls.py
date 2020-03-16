from django.urls import path
from django.conf.urls import include

from migrationcsv.views import html_to_pdf_view
from . import views

urlpatterns = [
	path("download/", html_to_pdf_view, name='download-pdf'),
	path("migration/", views.MigrationView.as_view(), name="migration"),
	path("appsec/", views.AppSecView.as_view(), name="appsec view"),
	path("findings/", views.FindingsListView.as_view(), name="findings list"),
	path("findings/<int:pk>/", views.FindingsDetailView.as_view(), name='findings-detail'),
	]