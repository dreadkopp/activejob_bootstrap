from .models import Kompetenzbereich
from core.views import SearchAndMenuDetailView


class KompetenzbereicheView(SearchAndMenuDetailView):
    model = Kompetenzbereich
    template_name = "web/pages/kompetenzbereiche.html"
