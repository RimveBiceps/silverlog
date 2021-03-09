from django import forms

class CompanySearchForm(forms.Form):
    company_title = forms.CharField(label='Company Title', max_length=15)