from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Job
from core.utils import MenuMixin
from .mixins import QuickSearchFormMixin, SearchMixin


class JobDetailView(QuickSearchFormMixin, MenuMixin, DetailView):
    model = Job
    template_name = "web/pages/stellenmarkt/job-detail.html"


class JobListView(QuickSearchFormMixin, MenuMixin, ListView):
    model = Job
    template_name = "web/pages/stellenmarkt.html"
    paginate_by = 10


class JobSearchListView(SearchMixin, JobListView):
    paginate_by = 10


class JobInternListView(JobListView):
    template_name = "web/pages/karriere_activjob.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_intern=True)
