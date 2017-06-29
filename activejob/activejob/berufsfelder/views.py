from .models import Berufsfelder
from core.views import SearchAndMenuDetailView


class BerufsfelderView(SearchAndMenuDetailView):
    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Berufsfelder",
        }

        if kwargs["variant"]:
            self.active_nodes["top"] = "bewerber"
            self.active_nodes["left"] = "bewerber_" + self.active_nodes["left"]

        return super().dispatch(request, *args, **kwargs)

    model = Berufsfelder
    template_name = "web/pages/berufsfelder.html"
