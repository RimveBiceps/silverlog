from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm


def handle_company(request):
    return render(request=request, template_name="alphavantage_api/company.html")
