from django import forms

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

    food_forms = Food.objects.order_by('food_form').values_list('food_form', flat=True).distinct()
    food_form = forms.ChoiceField(required=False, choices=enumerate(food_forms))
