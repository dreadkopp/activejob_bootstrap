from core.views import SearchAndMenuListView
from jobs.models import Location


class StandorteView(SearchAndMenuListView):
    template_name = "web/pages/standorte.html"
    model = Location
