from .models import Page
from core.views import SearchAndMenuDetailView, SearchAndMenuListView
from jobs.models import Job
from jobs.views import JobSearchListView


class ReferenzenView(SearchAndMenuDetailView):

    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Referenzen",
        }

        return super().dispatch(request, *args, **kwargs)

    template_name = "web/pages/referenzen.html"
    model = Page

class ReferenzenBlingView(JobSearchListView):

    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Referenzen",
        }

        return super().dispatch(request, *args, **kwargs)

    model = Job
    template_name = "web/pages/stellenmarkt.html"
    paginate_by = 10
