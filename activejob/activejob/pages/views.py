from core.views import SearchAndMenuDetailView
from .models import Page


class PageView(SearchAndMenuDetailView):
    template_name = "web/pages/page.html"
    model = Page
