from django.shortcuts import render
from django.views.generic import TemplateView

from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin
from .models import Locations

class StandorteView(QuickSearchFormMixin, MenuMixin, TemplateView):
    template_name = "web/pages/standorte.html"

    def get_context_data(self, **kwargs):
        context = super(StandorteView, self).get_context_data(**kwargs)
        context['standorte'] = Locations.locations
        return context
