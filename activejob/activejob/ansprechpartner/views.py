from django.shortcuts import render
from django.views.generic import DetailView, ListView


class AnsprechpartnerView(DetailView):
#    model = Job
    template_name = "web/test/test.html"
