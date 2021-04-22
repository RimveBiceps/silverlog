from django.urls import path
from . import views

app_name = 'alphavantage_api'

urlpatterns = [
    path("company", views.handle_company, name="company"),
    path("company_acronyms", views.handle_company_acronym, name="company_acronyms"),
    path('favorite/', views.fav_company),  # IP:PORT/company_symbol your post api to save favorite companies
    path("favorite_companies", views.handle_favorite_companies, name="favorite_companies"),

]
