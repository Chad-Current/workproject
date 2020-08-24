from django.http import HttpResponse, HttpResponseRedirect, FileResponse
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.urls import reverse
from django.views import generic
from django.views.generic import ListView, TemplateView
from django.db.models import Q
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django import forms
from django.conf import settings
from .models import Interoperability, IsicApplicant, Site
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.decorators import method_decorator
from django.core.paginator import Paginator
import os
import json
import cv2
import requests
from django.core.mail import send_mail

# send_mail(
#     'Subject here',
#     'Here is the message.',
#     'website@example.com',
#     ['current@dps.state.ia.us'],
#     fail_silently=False,
# )
# EMAIL ADRESS IsicsAdmin@dps.state.ia.us

# def home(request):
#     return render(request, 'isicwebdatabase/base.html')

# Loaded after signin
@login_required
def index(request):
    URL = "https://api.safetyculture.io/audits/search?field=audit_id&field=modified_at"
    header = {"Authorization": "Bearer 7a7a703f53a48c445b3af13f06fcff8076395f865a628f3716a2a9c0e89a9061"}
    initial_request = requests.get(URL, headers=header)
    key_value = initial_request.json()['audits'][0]
    context = {'context': key_value}
    return render(request, 'isicwebdatabase/index.html', context)

@login_required
def reports(request):
    return render(request, 'isicwebdatabase/genisisreport.html')

@login_required
def pdf_report(request, pdf_file):
    model = RenderPDF
    if "GET" == request.method:
        try:
            filename = RenderPDF.pdf_file + ".pdf"
            filepath = os.path.join(settings.MEDIA_ROOT, "records", filename)
            print(filepath)
            return FileResponse(open(filepath, 'rb'), content_type='application/pdf')
        except FileNotFoundError:
            messages.error(request, "Record not found ")
            return HttpResponseRedirect(reverse("isicwebdatabase:site-home-info", args=(pdf_file,)))
    else:
        return render(request, "isicwebdatabase:site-home-info")


class SiteTraining(LoginRequiredMixin, TemplateView):
    template_name = 'isicwebdatabase/sitetraining.html'
    # Point of Contacts Page

class PocHomeView(TemplateView):
    template_name = 'isicwebdatabase/poc.html'

class PocSearchViewCounty(LoginRequiredMixin, ListView):
    model = Interoperability
    template_name = 'isicwebdatabase/poc.html'


    def get_queryset(self): # new
        query = self.request.GET.get('county')
        object_list = Interoperability.objects.filter(county__istartswith=query)
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list


class PocSearchViewPoc(LoginRequiredMixin, ListView):
    model = Interoperability
    template_name = 'isicwebdatabase/poc.html'

    def get_queryset(self): # new
        query = self.request.GET.get('pointofcontact')
        object_list = Interoperability.objects.filter(Q(name__istartswith=query) | Q(name__iendswith=query))
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list


class PocSearchViewOrg(LoginRequiredMixin, ListView):
    model = Interoperability
    template_name = 'isicwebdatabase/poc.html'


    def get_queryset(self): # new
        query = self.request.GET.get('organization')
        object_list = Interoperability.objects.filter(Q(organization__istartswith=query) | Q(organization__iendswith=query))
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list


class PocSearchViewLevel(LoginRequiredMixin, ListView):
    model = Interoperability
    template_name = 'isicwebdatabase/poc.html'


    def get_queryset(self):
        query = self.request.GET.get('level')
        object_list = Interoperability.objects.filter(user_lvl__contains=query)
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list



class ApplicantView(LoginRequiredMixin, ListView):
    model = IsicApplicant
    template_name = 'isicwebdatabase/applicants.html'

    context_object_name = 'application'  # Default: object_list
    paginate_by = 10
    queryset = IsicApplicant.objects.all().order_by('applicant')  # Default: Model.objects.all()

class SiteHomeView(TemplateView):
    template_name = 'isicwebdatabase/siteinformation.html'


class SiteNameView(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'isicwebdatabase/siteinformation.html'

    def get_queryset(self):
        query = self.request.GET.get('site_name')
        object_list = Site.objects.filter(site_name__icontains=query)
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list

# class SiteAliasView(LoginRequiredMixin, ListView):
#     model = Site
#     template_name = 'isicwebdatabase/siteinformation.html'
#
#     def get_queryset(self):
#         query = self.request.GET.get('sitealias')
#         object_list = Site.objects.filter(site_alias__iexact=query)
#         if not object_list:
#             messages.warning(self.request, 'No Results Found')
#         return object_list

class SiteIdView(LoginRequiredMixin, ListView):
    model = Site
    template_name = 'isicwebdatabase/siteinformation.html'

    def get_queryset(self):
        query = self.request.GET.get('site_id')
        object_list = Site.objects.filter(site_id__iexact=query).order_by('site_id')
        if not object_list:
            messages.warning(self.request, 'No Results Found')
        return object_list






     # Python Example using Task Module for ZohoProjects Task Data Pull
#Begin by importing the "requests" module

# import requests
# #Set the Request Method
#  method = "GET";
# #Set the headers
#  headers = {'Authorization': 'Zoho-oauthtoken <YOUR_ACCESS_TOKEN>'}
# #Set the URL and Parameters to GET, POST and DELETE using Request Method
# url = ""; params = ""; r = ""; files = "";
#  if method=="GET":
#  url = "https://projectsapi.zoho.com/restapi/portal/[PORTALID]/projects/[PROJECTID]/tasks/"
#  params = {"index":1, "range":3}
#  r = requests.get(url, params=params, headers=headers);
#  elif method=="POST":
#  url = "https://projectsapi.zoho.com/restapi/portal/[PORTALID]/projects/[PROJECTID]/tasks/"
#  params = {"name":"Client Call"}
# #To attach files,if any
#  files = {"uploaddoc": open("samplefile.jpg", "rb")}
#  r = requests.post(url, params=params, headers=headers, files=files);
#  elif method=="DELETE":
#  url = "https://projectsapi.zoho.com/restapi/portal/[PORTALID]/projects/[PROJECTID]/tasks/[TASKID]/"
#  r = requests.delete(url, headers=headers);
# #Response HTTP Status Code
#  print "Response HTTP Status Code : ", r.status_code
# #Response Body
#  print "Response Body : ", r.content
