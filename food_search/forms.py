from django import forms


class SearchForm(forms.Form):
    q = forms.CharField(max_length=100, required=False, label='', )
    fda = forms.BooleanField(required=False, label='Meets FDA guidelines', initial=True)
    # breed_choices = Food.objects.order_by('breed').values_list('breed', flat=True).distinct()

    breed_choices = enumerate(['Any',
                               'Extra Small & Toy Breeds',
                               'Small Breeds',
                               'Medium Breeds',
                               'Large Breeds',
                               'Giant Breeds',
                               ])
    breed_size = forms.ChoiceField(choices=breed_choices)
