from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import constants
from .forms import CompanySearchForm
import requests
import json
import pandas as pd
from django.contrib.staticfiles import finders


@login_required
def handle_company(request):
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
        # if a POST (or any other method) we'll create a blank form
        else:
            form = CompanySearchForm()

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

@login_required
def handle_company_acronym(request):
    symbols_file = finders.find('main/nasdaq_screener_1619112811294.csv')

    df = pd.read_csv(symbols_file)
    df_list = [x if not 'nan' in x else '' for x in df.values]

    return render(request=request, template_name="alphavantage_api/company_acronyms.html", context={'pd_company_acronyms': df_list})
