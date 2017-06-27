from django.shortcuts import render
from django.views.generic import ListView

from .models import Berufsfelder
from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin

class BerufsfelderView(QuickSearchFormMixin, MenuMixin, ListView):
    model = Berufsfelder
    template_name = "web/pages/berufsfelder.html"
