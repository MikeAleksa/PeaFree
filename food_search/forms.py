from django import forms
from django.db.models import Count

from .models import Food


class SearchForm(forms.Form):
    # should de-couple CSS from form - how?
    q = forms.CharField(max_length=100, required=False, label='',
                        widget=forms.TextInput(attrs={'class': 'searchbar border-bottom',
                                                      'placeholder': 'Search All Foods'}))
    fda = forms.BooleanField(required=False, label='Meets FDA Guidelines')
    xsm = forms.BooleanField(required=False, label='Extra Small & Toy Breeds')
    sm = forms.BooleanField(required=False, label='Small Breeds')
    md = forms.BooleanField(required=False, label='Medium Breeds')
    lg = forms.BooleanField(required=False, label='Large Breeds')
    xlg = forms.BooleanField(required=False, label='Giant Breeds')

    food_form = forms.ModelChoiceField(required=False, label='Food Form',
                                       queryset=Food.objects.values_list('food_form', flat=True).annotate(
                                           count=Count('food_form')).order_by('-count').distinct())
