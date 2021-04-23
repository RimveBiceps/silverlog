from django import forms
from .models import FavoriteCompanies

TIME_CHOICES= [
    ('TIME_SERIES_DAILY', 'Daily'),
    ('TIME_SERIES_WEEKLY', 'Weekly'),
    ('TIME_SERIES_MONTHLY', 'Monthly')
    ]

class CompanySearchForm(forms.Form):
    company_title = forms.CharField(label='Company Title', max_length=15)

class GraphsForm(forms.Form):
    company_title = forms.ModelChoiceField(queryset=FavoriteCompanies.objects.all())
    time_series = forms.CharField(label='Time series', widget=forms.Select(choices=TIME_CHOICES))

    def __init__(self, user, *args, **kwargs):
        super(GraphsForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['company_title'].queryset = FavoriteCompanies.objects.filter(user_id=user)
