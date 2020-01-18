from django.db.models import Max
from django.views import generic

from .models import Food, ScraperUpdates


class IndexView(generic.TemplateView):
    # TODO: add search functionality
    template_name = 'food_search/index.html'
    extra_context = {
        'food_count': Food.objects.count(),
        'good_count': Food.objects.filter(fda_guidelines=1).count(),
        'update': ScraperUpdates.objects.all().aggregate(Max('date')),
    }


class ResultsView(generic.ListView):
    template_name = 'food_search/results.html'
    context_object_name = 'results'
    queryset = Food.objects.filter(fda_guidelines=True).order_by('name')
    extra_context = {'total_results': queryset.count()}
    paginate_by = 50
