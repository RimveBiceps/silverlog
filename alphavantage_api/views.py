from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from . import constants
from .forms import CompanySearchForm
import requests
import json


def handle_company(request):
    # if a POST (or any other method) we'll create a blank form
    form = CompanySearchForm()
    context = {}
    if request.method == "GET":
        # create a form instance and populate it with data from the request:
        form = CompanySearchForm(request.GET)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            company_acronym = form.cleaned_data['company_title']
            company_data = make_api_request(company_acronym)
            if not company_data:
                messages.error(request, "Company doesn't exist.")
            else:
                context["company_result_data"] = company_data
            
    context["form"] = form
    return render(request=request, template_name="alphavantage_api/company.html", context=context)


def make_api_request(company_acronym):
    data = {
        "function": "OVERVIEW",
        "symbol": company_acronym,
        "apikey": constants.API_KEY
    }
    response = requests.get(constants.API_URL, data)
    response_json = response.json()

    return response_json
