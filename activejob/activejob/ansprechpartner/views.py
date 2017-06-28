from .models import Ansprechpartner
from core.views import SearchAndMenuDetailView

class AnsprechpartnerView(SearchAndMenuDetailView):
    model = Ansprechpartner
    template_name = "web/pages/ansprechpartner.html"
