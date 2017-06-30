from core.views import SearchAndMenuDetailView
from .models import Page
from core.utils import build_main_menu


class PageView(SearchAndMenuDetailView):

    template_name = "web/pages/page.html"
    model = Page

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        p = self.object
        self.active_nodes = {
            "top": p.menu_top_entry,
            "left": p.menu_left_entry,
            "sub": p.menu_left_sub_entry,
        }

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
