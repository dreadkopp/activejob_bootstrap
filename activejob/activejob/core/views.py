from django.views.generic import CreateView, DetailView, ListView, TemplateView
from .mixins import MenuMixin
from jobs.mixins import QuickSearchFormMixin
from .utils import menu_items


class SearchAndMenuCreateView(QuickSearchFormMixin, MenuMixin, CreateView):
    pass


class SearchAndMenuDetailView(QuickSearchFormMixin, MenuMixin, DetailView):
    pass


class SearchAndMenuListView(QuickSearchFormMixin, MenuMixin, ListView):
    pass


class SearchAndMenuTemplateView(QuickSearchFormMixin, MenuMixin, TemplateView):
    pass

class SitemapView(SearchAndMenuTemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"menu_left_sm": menu_items})
        return context
