from django.contrib.syndication.views import Feed

from .mixins import SearchMixin
from .models import Job
from core.views import SearchAndMenuDetailView, SearchAndMenuListView


class JobDetailView(SearchAndMenuDetailView):
    model = Job
    template_name = "web/pages/stellenmarkt/job-detail.html"


class JobListView(SearchAndMenuListView):
    model = Job
    template_name = "web/pages/stellenmarkt.html"
    paginate_by = 10


class JobSearchListView(SearchMixin, JobListView):
    paginate_by = 10

    def dispatch(self, request, *args, **kwargs):
        for department in ["aü", "av", "pv"]:
            if department in request.GET:
                request.session["stellenmarkt_department"] = department
                break

        return super().dispatch(request, *args, **kwargs)


class JobInternListView(JobListView):
    template_name = "web/pages/karriere_activjob.html"

    def get_queryset(self):
        return super().get_queryset().filter(is_intern=True)


class RSSFeed(Feed):
    title = "Stellenmarkt activjob GmbH"
    link = "https://www.activ-job.com"
    description =  "Stellenmarkt activjob GmbH"

    def items(self):
        return Job.objects.all()

    def item_title(self, item):
        return item.title

    def item_description(self, item):
        return item.description
