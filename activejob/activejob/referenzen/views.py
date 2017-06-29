from .models import Page
from core.views import SearchAndMenuDetailView

class ReferenzenView(SearchAndMenuDetailView):
    template_name = "web/pages/referenzen.html"
    model = Page
