from django.views.generic import DetailView, ListView, TemplateView
from .mixins import MenuMixin
from jobs.mixins import QuickSearchFormMixin


class SearchAndMenuDetailView(QuickSearchFormMixin, MenuMixin, DetailView):
    pass


class SearchAndMenuListView(QuickSearchFormMixin, MenuMixin, ListView):
    pass


class SearchAndMenuTemplateView(QuickSearchFormMixin, MenuMixin, TemplateView):
    pass
