from .models import Kompetenzbereich
from core.views import SearchAndMenuDetailView


class KompetenzbereicheView(SearchAndMenuDetailView):
    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Kompetenzbereiche",
        }
        
        return super().dispatch(request, *args, **kwargs)

    model = Kompetenzbereich
    template_name = "web/pages/kompetenzbereiche.html"
