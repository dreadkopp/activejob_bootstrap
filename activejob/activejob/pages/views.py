from core.views import SearchAndMenuDetailView
from .models import Page
from core.utils import build_main_menu


class PageView(SearchAndMenuDetailView):

    template_name = "web/pages/page.html"
    model = Page

    def get_context_data(self, **kwargs):
        p = self.object
        self.active_nodes = {
            "top": p.menu_top_entry,
            "left": p.menu_left_entry,
            "sub": p.menu_left_sub_entry,
        }
        return super().get_context_data(**kwargs)
