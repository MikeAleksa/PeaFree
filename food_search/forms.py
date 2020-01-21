from django import forms

from .models import Food


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label='',
                        widget=forms.TextInput(attrs={'class': 'searchbar rounded btn-lg',
                                                      'placeholder': 'Search...'}))
    fda = forms.BooleanField(required=False, label='Meets FDA Guidelines', initial=True)
    xsm = forms.BooleanField(required=False, label='Extra Small & Toy Breeds')
    sm = forms.BooleanField(required=False, label='Small Breeds')
    md = forms.BooleanField(required=False, label='Medium Breeds')
    lg = forms.BooleanField(required=False, label='Large Breeds')
    xlg = forms.BooleanField(required=False, label='Giant Breeds')

    food_forms = Food.objects.order_by('food_form').values_list('food_form', flat=True).distinct()
    food_form = forms.ChoiceField(choices=enumerate(food_forms))
