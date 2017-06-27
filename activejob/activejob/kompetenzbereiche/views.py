from django.shortcuts import render
from django.views.generic import DetailView

from .models import Kompetenzbereiche
from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin

class KompetenzbereicheView(QuickSearchFormMixin, MenuMixin, DetailView):
    model = Kompetenzbereiche
    template_name = "web/pages/kompetenzbereiche.html"
