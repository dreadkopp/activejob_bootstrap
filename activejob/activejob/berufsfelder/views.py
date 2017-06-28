from .models import Berufsfelder
from core.views import SearchAndMenuDetailView

class BerufsfelderView(SearchAndMenuDetailView):
    model = Berufsfelder
    template_name = "web/pages/berufsfelder.html"
