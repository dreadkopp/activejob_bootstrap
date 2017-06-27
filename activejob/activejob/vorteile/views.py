from django.shortcuts import render
from django.views.generic import DetailView

from core.utils import MenuMixin
from jobs.mixins import QuickSearchFormMixin
from .models import Vorteile

class VorteileView(QuickSearchFormMixin, MenuMixin, DetailView):
    model = Vorteile
    template_name = "web/pages/vorteile.html"
