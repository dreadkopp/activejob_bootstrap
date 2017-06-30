from core.views import SearchAndMenuDetailView
from .models import Page
from core.utils import build_main_menu


class PageView(SearchAndMenuDetailView):

    template_name = "web/pages/page.html"
    model = Page

    def dispatch(self, request, *args, **kwargs):
        self.active_nodes = {
            "top": Page.menu_top_entry,
            "left": Page.menu_left_entry,
            "sub": Page.menu_left_sub_entry,
        }

        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context.update({"top": Page.menu_top_entry, "left": Page.menu_left_entry, "sub": Page.menu_left_sub_entry})
        return context
