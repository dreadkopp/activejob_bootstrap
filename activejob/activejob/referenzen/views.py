from .models import Field
from core.views import SearchAndMenuListView

class ReferenzenView(SearchAndMenuListView):
    template_name = "web/pages/referenzen.html"
    model = Field
