from .models import Page
from core.views import SearchAndMenuDetailView


class ReferenzenView(SearchAndMenuDetailView):

    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Referenzen",
        }

        if kwargs["variant"]:
            self.active_nodes["top"] = "bewerber"
            self.active_nodes["left"] = "bewerber_" + self.active_nodes["left"]

        return super().dispatch(request, *args, **kwargs)

    template_name = "web/pages/referenzen.html"
    model = Page
