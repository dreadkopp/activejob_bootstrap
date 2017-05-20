from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Job

class JobDetailView(DetailView):
    model = Job
    template_name = "web/pages/stellenmarkt/job-detail.html"


class JobListView(ListView):
    model = Job
    template_name = "web/pages/stellenmarkt.html"
    paginate_by = 10
