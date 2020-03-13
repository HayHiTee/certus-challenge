from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from .modelform import PasswordVaultForm
# Create your views here.


class PasswordVaultView(APIView):
	def get(self, request):
		form = PasswordVaultForm()
		self.templateName = "migrationcsv/insights/webinar.html"
		return render(request, self.templateName, {'form': form})

	def post(self, request):
		form = PasswordVaultForm(request.POST)
		self.templateName = "migrationcsv/insights/webinar.html"
		return render(request, self.templateName)

