from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Job
from core.utils import MenuMixin
from .mixins import SearchMixin


class JobDetailView(MenuMixin, DetailView):
    model = Job
    template_name = "web/pages/stellenmarkt/job-detail.html"


class JobListView(MenuMixin, ListView):
    model = Job
    template_name = "web/pages/stellenmarkt.html"
    paginate_by = 10


class JobSearchListView(SearchMixin, JobListView):
    paginate_by = 10
