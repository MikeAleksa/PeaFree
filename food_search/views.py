import operator
from functools import reduce

from django.db.models import Max, Q
from django.views import generic

from .forms import SearchForm
from .models import Food, ScraperUpdates


class IndexView(generic.TemplateView):
    template_name = 'food_search/index.html'
    extra_context = {
        'food_count': Food.objects.count(),
        'good_count': Food.objects.filter(fda_guidelines=1).count(),
        'update': ScraperUpdates.objects.all().aggregate(Max('date')),
        'form': SearchForm()
    }


class ResultsView(generic.ListView):
    template_name = 'food_search/results.html'
    context_object_name = 'results'
    paginate_by = 25

    def get_q(self):
        return self.request.GET.get('q', None)

    def get_fda(self):
        return self.request.GET.get('fda', 'on')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get search variables from current page (i.e. from GET request) - for use in pagination
        search_vars = []
        if self.request.GET.items():
            for key, value in self.request.GET.items():
                if key != "page":
                    search_vars.append("{}={}".format(key, value))
            context['search_vars'] = '&'.join(search_vars)
        return context

    def get_queryset(self):
        queryset = Food.objects.all()
        query_list = self.get_q()

        # if a search query was made, split it into words and filter
        if query_list:
            query_list = query_list.split()
            queryset = queryset.filter(reduce(operator.and_, (Q(name__icontains=q) for q in query_list)))

        # filter by FDA guidelines
        if self.request.GET.get('fda') == 'on':
            queryset = queryset.filter(fda_guidelines=True)

        return queryset.order_by('name')
