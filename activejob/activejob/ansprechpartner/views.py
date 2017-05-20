from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Ansprechpartner

class AnsprechpartnerView(DetailView):
    model = Ansprechpartner
    template_name = "web/test/test.html"
