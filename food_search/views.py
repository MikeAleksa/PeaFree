from django.db.models import Max
from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Food, Diet, ScraperUpdates


def index(request):
    context = {
        'food_count': Food.objects.count(),
        'good_count': Food.objects.filter(fda_guidelines=1).count(),
        'update': ScraperUpdates.objects.all().aggregate(Max('date')),
    }
    # TODO: search functionality
    return render(request, 'food_search/index.html', context)


def detail(request, item_num):
    food = get_object_or_404(Food, item_num=item_num)
    sizes = list()
    for size, name in [
        (food.xsm_breed, Food._meta.get_field('xsm_breed').verbose_name),
        (food.sm_breed, Food._meta.get_field('sm_breed').verbose_name),
        (food.md_breed, Food._meta.get_field('md_breed').verbose_name),
        (food.lg_breed, Food._meta.get_field('lg_breed').verbose_name),
        (food.xlg_breed, Food._meta.get_field('xlg_breed').verbose_name),
    ]:
        if size == 1:
            sizes.append(name.title())
    context = {
        'food': food,
        'breed_sizes': ', '.join(sizes)
    }
    return render(request, 'food_search/detail.html', context)


def results(request):
    # TODO: results of a search
    context = {
        'results': Food.objects.all().order_by('name')
    }
    return render(request, 'food_search/results.html', context)


def about(request):
    # TODO: about the site
    return HttpResponse('Information about application here.')


def disclaimer(request):
    # TODO: about the site
    return HttpResponse('Disclaimer: use this information at your own discretion. It is not guaranteed to be correct.')
