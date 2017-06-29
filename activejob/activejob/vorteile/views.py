from .models import Vorteile
from core.views import SearchAndMenuDetailView


class VorteileView(SearchAndMenuDetailView):
    model = Vorteile
    template_name = "web/pages/vorteile.html"
