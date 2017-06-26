def build_main_menu (active_node=None, submenu=None):
    menu_top = [
        {
            "name": "",
            "active": True,
            "url": "home",
            "class": "glyphicon glyphicon-home",
        },
        {
            "name": "Über uns",
            "url": "unternehmensprofil",
        },
        {
            "name": "Unternehmen",
            "url": "unternehmen",
        },
        {
            "name": "Bewerber",
            "url": "bewerber",
        },
    ]

    menu_left = []

    return {
        "menu_top": menu_top,
        "menu_left": menu_left,
    }


class MenuMixin:
    active_node = None
    submenu = None

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = build_main_menu(
            active_node=self.active_node,
            submenu=self.submenu,
        )
        context.update(menu_context)
        return context
