from .utils import build_main_menu


class MenuMixin:
    active_nodes = {pos: None for pos in ["top", "left", "sub"]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = build_main_menu(
            active_nodes=self.active_nodes,
        )
        context.update(menu_context)
        return context
