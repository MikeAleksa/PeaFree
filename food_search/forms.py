from django import forms
from django.db.models import Count

from .models import Diet, Food


class SearchForm(forms.Form):
    # should de-couple CSS from form - how?
    q = forms.CharField(max_length=100, required=False, label='',
                        widget=forms.TextInput(attrs={'class': 'searchbar border-bottom',
                                                      'placeholder': 'Search All Foods'}))

    fda = forms.BooleanField(required=False, label='Meets FDA Guidelines')

    # breed sizes
    xsm = forms.BooleanField(required=False, label='Extra Small & Toy Breeds')
    sm = forms.BooleanField(required=False, label='Small Breeds')
    md = forms.BooleanField(required=False, label='Medium Breeds')
    lg = forms.BooleanField(required=False, label='Large Breeds')
    xlg = forms.BooleanField(required=False, label='Giant Breeds')

    # food forms
    all_food_forms = Food.objects.values_list('food_form', flat=True).annotate(count=Count('food_form')).order_by(
        '-count')
    all_food_forms = [('', '')] + [(f, f) for f in all_food_forms][:10]
    food_form = forms.ChoiceField(required=False, label='Food Form', choices=all_food_forms)

    # brands
    all_brands = Food.objects.values_list('brand', flat=True).distinct().order_by('brand')
    all_brands = [('', '')] + [(b, b) for b in all_brands]
    brand = forms.ChoiceField(required=False, label='Brand', choices=all_brands)

    # lifestages
    all_lifestages = Food.objects.values_list('lifestage', flat=True).distinct().order_by('lifestage')
    split_lifestages = set()
    split_lifestages.add(('', ''))
    for lifestage in all_lifestages:
        for lifestage_split in lifestage.split(', '):
            split_lifestages.add((lifestage_split, lifestage_split))
    lifestage = forms.ChoiceField(required=False, label='Lifestage', choices=sorted(split_lifestages))

    # special diet
    all_diets = Diet.objects.values_list('diet', flat=True).annotate(count=Count('diet')).order_by(
        '-count')
    all_diets = [('', '')] + [(d, d) for d in all_diets]
    diet = forms.ChoiceField(required=False, label='Special Diet', choices=sorted(all_diets))
