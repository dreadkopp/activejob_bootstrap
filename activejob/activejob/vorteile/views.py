from .models import Vorteile
from core.views import SearchAndMenuDetailView


class VorteileView(SearchAndMenuDetailView):

    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Ihre Vorteile",
        }

        if kwargs["variant"]:
            self.active_nodes["top"] = "bewerber"
            self.active_nodes["left"] = "bewerber_" + self.active_nodes["left"]

        return super().dispatch(request, *args, **kwargs)

    model = Vorteile
    template_name = "web/pages/vorteile.html"
