from django.shortcuts import render
from django.views.generic import DetailView

from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin
from .models import Locations

class StandorteView(QuickSearchFormMixin, MenuMixin, DetailView):
    model = Locations
    template_name = "web/pages/standorte.html"
