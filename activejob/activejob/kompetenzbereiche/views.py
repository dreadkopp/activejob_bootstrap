from .models import Kompetenzbereich
from core.views import SearchAndMenuDetailView


class KompetenzbereicheView(SearchAndMenuDetailView):
    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Kompetenzbereiche",
        }

        if kwargs["variant"]:
            self.active_nodes["top"] = "bewerber"
            self.active_nodes["left"] = "bewerber_" + self.active_nodes["left"]

        return super().dispatch(request, *args, **kwargs)

    model = Kompetenzbereich
    template_name = "web/pages/kompetenzbereiche.html"
