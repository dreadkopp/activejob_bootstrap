from .models import Vorteile
from core.views import SearchAndMenuDetailView


class VorteileView(SearchAndMenuDetailView):

    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "bewerber",
            "left": kwargs["slug"],
            "sub": "Ihre Vorteile",
        }

        return super().dispatch(request, *args, **kwargs)

    model = Vorteile
    template_name = "web/pages/vorteile.html"
