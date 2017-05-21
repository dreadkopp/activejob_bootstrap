from django.shortcuts import render
from django.views.generic import DetailView

from .models import Berufsfelder

class BerufsfelderView(DetailView):
    model = Berufsfelder
    template_name = "web/pages/berufsfelder.html"
