from django.shortcuts import render
from django.views.generic import DetailView

from .models import Kompetenzbereiche

class KompetenzbereicheView(DetailView):
    model = Kompetenzbereiche
    template_name = "web/page/kompetenzbereiche.html"
