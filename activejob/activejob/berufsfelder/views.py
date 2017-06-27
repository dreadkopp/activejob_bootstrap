from django.shortcuts import render
from django.views.generic import DetailView

from .models import Berufsfelder
from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin

class BerufsfelderView(QuickSearchFormMixin, MenuMixin, DetailView):
    model = Berufsfelder
    template_name = "web/pages/berufsfelder.html"
