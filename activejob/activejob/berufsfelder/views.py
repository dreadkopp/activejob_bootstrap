from .models import Berufsfelder
from core.views import SearchAndMenuDetailView


class BerufsfelderView(SearchAndMenuDetailView):
    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": "bewerber",
            "left": kwargs["slug"],
            "sub": "Berufsfelder",
        }

        return super().dispatch(request, *args, **kwargs)

    model = Berufsfelder
    template_name = "web/pages/berufsfelder.html"
