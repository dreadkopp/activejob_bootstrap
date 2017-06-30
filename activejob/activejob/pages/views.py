from core.views import SearchAndMenuDetailView
from .models import Page
from core.utils import build_main_menu


class PageView(SearchAndMenuDetailView):

    template_name = "web/pages/page.html"
    model = Page

    def get_object(self):
        the_object = super().get_object()

        p = the_object
        self.active_nodes = {
            "top": p.menu_top_entry,
            "left": p.menu_left_entry,
            "sub": p.menu_left_sub_entry,
        }

        return the_object
