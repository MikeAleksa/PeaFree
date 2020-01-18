from collections import defaultdict

from django.db.models import Max
from django.shortcuts import get_list_or_404, get_object_or_404, render

from .models import Food, Diet, ScraperUpdates


def index(request):
    context = {
        'food_count': Food.objects.count(),
        'good_count': Food.objects.filter(fda_guidelines=1).count(),
        'update': ScraperUpdates.objects.all().aggregate(Max('date')),
    }
    # TODO: search functionality
    return render(request, 'food_search/index.html', context)


def results(request):
    # TODO: results of a search
    # TODO: pages of results
    foods = Food.objects.all().order_by('name').filter(fda_guidelines=True)
    context = {
        'results': foods
    }
    return render(request, 'food_search/results.html', context)
