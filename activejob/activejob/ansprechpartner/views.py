from django.shortcuts import render
from django.views.generic import DetailView

from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin
from .models import Ansprechpartner

class AnsprechpartnerView(QuickSearchFormMixin, MenuMixin, DetailView):
    model = Ansprechpartner
    template_name = "web/pages/ansprechpartner.html"
