from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label='', )
    fda = forms.BooleanField(required=False, initial=True, label='Meets FDA Guidelines')
