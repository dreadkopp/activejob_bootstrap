from django.shortcuts import render
from django.views.generic import ListView
from .models import Job
from jobs.mixins import QuickSearchFormMixin
from core.utils import MenuMixin

class ReferenzenView(QuickSearchFormMixin, MenuMixin, ListView):
    template_name = "web/pages/referenzen.html"
    model = Job
