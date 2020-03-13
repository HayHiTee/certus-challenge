import pdfkit
from django.shortcuts import render, redirect
from django.core.exceptions import ValidationError
from django.http import JsonResponse, Http404, HttpResponseNotFound
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.views import generic

from rest_framework.views import APIView
from rest_framework.parsers import JSONParser

from .models import Findings

import json

from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
import os
from django.conf import settings


def html_to_pdf_view(request, pk):
    download_format = request.GET.get('format', 'PDF').upper()
    if download_format == "PDF" or download_format == "HTML":
        content_type = "text/html"
        finding_object = Findings.objects.get(id=pk)
        output = render_to_string('migrationcsv/pdf_templates.html', {'object': finding_object})
        # convert html to pdf if user requests for pdf
        if download_format == "PDF":
            content_type = 'application/pdf'
            output = pdfkit.from_string(output, False)
        response = HttpResponse(output, content_type=content_type)
        response['Content-Disposition'] = f'attachment; filename="finding_details.{download_format.lower()}"'
        return response
    else:

        return HttpResponseNotFound('Format Type not Supported')





class AppSecView(generic.ListView):
    model = Findings
    template_name = 'migrationcsv/findings_list.html'


class FindingsListView(generic.ListView):
    model = Findings
    template_name = 'migrationcsv/findings_list.html'


class FindingsDetailView(generic.DetailView):
    model = Findings

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context


class MigrationView(APIView):
    @csrf_exempt
    def post(self, request):
        data = JSONParser().parse(request)
        metadata_ = Findings(finding_name=data['Findings'], description=data['Descrptions'], solution=data['Solutions'])
        metadata_.save()
        JsonResponse(data, status=201)

    #


# print (data.keys())
# metadata_ = Findings(findings_name = data['Findings'], description = data['Descrptions'], solution = data['Solutions'])
# metadata_.save()
# return JsonResponse(data, status=201)


'''

{"Findings": "XSS injection", "Descrptions": "Every time the application gets userinput, whether this showing it on screen or processing this data in the application background, these parameters should be escaped for malicious code in order to prevent crosssite scripting injections. When an attacker gains the possibility to perform an XSS injection, he is given the opportunity to inject HTML and JavaScript code directly into the application. This could lead to accounts being compromised by stealing session cookies or directly  affect the operation of the target application.   Altough templating engines(razor, twig, jinja, etc) and contextaware applications(Angular, React, etc) do a lot of auto escaping for you. These frameworks should always be validated for effectiveness.", "Solutions": "Every time the application gets userinput, whether this showing it on screen or processing this data in the application background, these parameters should be escaped for malicious code in order to prevent crosssite scripting injections. When an attacker gains the possibility to perform an XSS injection, he is given the opportunity to inject HTML and JavaScript code directly into the application. This could lead to accounts being compromised by stealing session cookies or directly  affect the operation of the target application.   Altough templating engines(razor, twig, jinja, etc) and contextaware applications(Angular, React, etc) do a lot of auto escaping for you. These frameworks should always be validated for effectiveness."}

'''
