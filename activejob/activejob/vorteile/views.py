from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Vorteile

class VorteileView(DetailView):
    model = Vorteile
    template_name = "web/pages/vorteile.html"
