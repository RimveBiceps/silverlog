from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from . import constants
from .forms import CompanySearchForm, GraphsForm
import requests
import json

import pandas as pd
from django.contrib.staticfiles import finders

from django.views.decorators.csrf import csrf_exempt
from alphavantage_api.models import FavoriteCompanies
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse

from .models import FavoriteCompanies

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
    df_list = [x for x in df.values]

    return render(request=request, template_name="alphavantage_api/company_acronyms.html", context={'pd_company_acronyms': df_list})

@login_required
@csrf_exempt
def fav_company(request):
    company_symbol = request.POST.get('company_symbol')
    if not company_symbol:
        raise ValueError("Required company_symbol to set company as favorite")

    user_id = request.user.pk
    try:
        fav_companies_obj = {
            'user_id': user_id,
            'company_acr': company_symbol
        }
        FavoriteCompanies(**fav_companies_obj).save()
    except ObjectDoesNotExist:
        # raise or Return HTTP response with failure status_code
        return HttpResponse('Some error occured, unable to add to wishlist') ## or can set for render
        
    return HttpResponse('Added to favorites!') # or can set for render

@login_required
def handle_favorite_companies(request):
    context = {}
    fav_companies_list = FavoriteCompanies.objects.filter(user_id=request.user.pk)
    context['fav_comp'] = fav_companies_list

    return render(request=request, template_name="alphavantage_api/favorite_companies.html", context=context)

@login_required
def handle_graphs(request):
    context = {}
    if request.method == "GET":
        # create a form instance and populate it with data from the request:
        form = GraphsForm(request.user.pk, request.GET)
        if form.is_valid():
            # process the data in form.cleaned_data as required
            company_title = form.cleaned_data['company_title']
            time_series = form.cleaned_data['time_series']
            data = {
                "function": time_series,
                "symbol": company_title,
                "apikey": constants.API_KEY
            }
            response = requests.get(constants.API_URL, data)
            response_json = response.json()
            if not response_json:
                messages.error(request, "Something went wrong...")
            else:
                context["graph_result_data"] = response_json
                print(list(response_json.keys()))
        # if a POST (or any other method) we'll create a blank form
        else:
            form = GraphsForm(request.user.pk)

    context["form"] = form
    return render(request=request, template_name="alphavantage_api/graphs.html", context=context)
