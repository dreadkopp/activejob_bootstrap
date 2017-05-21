from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Kompetenzbereiche

class KompetenzbereicheView(DetailView):
    model = Kompetenzbereiche
    template_name = "web/page/kompetenzbereiche.html"
