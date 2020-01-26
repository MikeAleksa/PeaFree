import operator
from functools import reduce

from django.db.models import Max, Q
from django.views import generic

from .forms import SearchForm
from .models import Food, ScraperUpdates


class IndexView(generic.TemplateView):
    form_class = SearchForm
    template_name = 'food_search/index.html'
    extra_context = {
        'food_count': Food.objects.count(),
        'good_count': Food.objects.filter(fda_guidelines=1).count(),
        'update': ScraperUpdates.objects.all().aggregate(Max('date')),
        'form': form_class()
    }


class ResultsView(generic.ListView):
    form_class = SearchForm
    template_name = 'food_search/results.html'
    context_object_name = 'results'
    paginate_by = 30

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        # get submitted form
        form = self.form_class(self.request.GET)
        context['form'] = form

        # get previous search - so they aren't lost during pagination
        context['search_vars'] = self.get_previous_search_vars()

        return context

    def get_previous_search_vars(self):
        # get search variables from current page (i.e. from GET request)
        search_vars = []
        if self.request.GET.items():
            for key, value in self.request.GET.items():
                if key != "page" and value is not None:
                    search_vars.append("{}={}".format(key, '+'.join(value.split())))
            return '&'.join(search_vars)

    def get_queryset(self):
        queryset = Food.objects

        # if a search query was made, split it into words and filter
        query_list = self.request.GET.get('q', None)
        if query_list:
            query_list = query_list.split()
            queryset = queryset.filter(reduce(operator.and_, (Q(name__icontains=q) for q in query_list)))

        # filter by FDA guidelines
        if self.request.GET.get('fda', None) == 'on':
            queryset = queryset.filter(fda_guidelines=True)

        # filter by breed size
        for size in ['xsm', 'sm', 'md', 'lg', 'xlg']:
            if self.request.GET.get(size, None) == 'on':
                queryset = queryset.filter(**{str(size + '_breed'): True})

        # filter by brand

        # filter by food form
        if self.request.GET.get('food_form', str()) != str():
            form = ' '.join(self.request.GET.get('food_form').split('+'))
            queryset = queryset.filter(food_form=form)

        # filter by lifestage

        # filter by special diet

        # return ordered queryset
        return queryset.order_by('name')
