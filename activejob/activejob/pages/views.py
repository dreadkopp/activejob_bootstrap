from core.views import SearchAndMenuDetailView
from .models import Page
from core.utils import build_main_menu
from django.shortcuts import get_object_or_404


class PageView(SearchAndMenuDetailView):

    template_name = "web/pages/page.html"
    model = Page

    def dispatch(self, request, *args, **kwargs):
        response = super().dispatch(request, *args, **kwargs)
        p = get_object_or_404(Page, slug=kwargs['slug'])
        self.active_nodes = {
            "top": p.menu_top_entry,
            "left": p.menu_left_entry,
            "sub": p.menu_left_sub_entry,
        }
        
        return response
