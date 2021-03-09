from django.urls import path
from . import views

app_name = 'alphavantage_api'

urlpatterns = [
    path("company", views.handle_company, name="company"),
]
