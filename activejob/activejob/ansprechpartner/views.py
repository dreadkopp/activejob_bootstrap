from .models import Ansprechpartner
from core.views import SearchAndMenuDetailView


class AnsprechpartnerView(SearchAndMenuDetailView):
    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "unternehmen",
            "left": kwargs["slug"],
            "sub": "Ansprechpartner",
        }

        if kwargs["variant"]:
            self.active_nodes["top"] = "bewerber"
            self.active_nodes["left"] = "bewerber_" + self.active_nodes["left"]

        return super().dispatch(request, *args, **kwargs)

    model = Ansprechpartner
    template_name = "web/pages/ansprechpartner.html"

def karriereberatung(request):
    return AnsprechpartnerView.as_view(template_name="web/pages/karriereberatung.html")(request,variant="bewerber", slug="karriereberatung")
