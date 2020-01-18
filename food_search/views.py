from django.db.models import Max
from django.views import generic

from .models import Food, ScraperUpdates


class IndexView(generic.TemplateView):
    template_name = 'food_search/index.html'
    extra_context = {
        'food_count': Food.objects.count(),
        'good_count': Food.objects.filter(fda_guidelines=1).count(),
        'update': ScraperUpdates.objects.all().aggregate(Max('date')),
    }


class ResultsView(generic.ListView):
    template_name = 'food_search/results.html'
    context_object_name = 'results'
    paginate_by = 50

    def get_queryset(self):
        query = self.request.GET.get('q')
        queryset = Food.objects.filter(name__icontains=query)
        if self.request.GET.get('fda') == 'on':
            queryset = queryset.filter(fda_guidelines=True)
        return queryset.order_by('name')
