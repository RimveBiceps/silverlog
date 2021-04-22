from django.urls import path
from . import views

app_name = 'alphavantage_api'

urlpatterns = [
    path("company", views.handle_company, name="company"),
    path("company_acronyms", views.handle_company_acronym, name="company_acronyms"),
    path('favorite/', views.fav_company),  ## IP:PORT/mymusic your post api to save wishlist

]
