from django.views.generic import CreateView, DetailView, ListView, TemplateView
from .mixins import MenuMixin
from jobs.mixins import QuickSearchFormMixin


class SearchAndMenuCreateView(QuickSearchFormMixin, MenuMixin, CreateView):
    pass


class SearchAndMenuDetailView(QuickSearchFormMixin, MenuMixin, DetailView):
    pass


class SearchAndMenuListView(QuickSearchFormMixin, MenuMixin, ListView):
    pass


class SearchAndMenuTemplateView(QuickSearchFormMixin, MenuMixin, TemplateView):
    pass
