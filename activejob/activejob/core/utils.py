def build_main_menu (active_node=None, submenu=None):
    menu_top = [
        {
            "name": "Home",
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

    for item in menu_top:
        item["active"] = item["url"] == active_node

    menu_items = {
        "unternehmensprofil": [
            {
                "name": "Unternehmensprofil",
                "url": "unternehmensprofil"
            },
            {
                "name": "Leitbild",
                "url": "leitbild"
            },
            {
                "name": "Standorte",
                "url": "standorte"
            },
            {
                "name": "Kontakt",
                "url": "kontakt"
            },
        ],
        "unternehmen": [
            {
                "name": "Arbeitnehmerüberlassung",
                "url": "arbeitnehmerueberlassung"
            },
            {
                "name": "Personalvermittlung",
                "url": "personalvermittlung"
            },
            {
                "name": "Arbeitsvermittlung",
                "url": "arbeitsvermittlung"
            },
            {
                "name": "Personalanfrage",
                "url": "personalanfrage"
            },
            {
                "name": "Personalauswahl",
                "url": "personalauswahl"
            },
        ],
        "bewerber": [
            {
                "name": "Arbeitnehmerüberlassung",
                "url": "arbeitnehmerueberlassung"
            },
            {
                "name": "Personalvermittlung",
                "url": "personalvermittlung"
            },
            {
                "name": "Arbeitsvermittlung",
                "url": "arbeitsvermittlung"
            },
            {
                "name": "Karriereberatung",
                "url": "karriereberatung"
            },
            {
                "name": "Stellenmarkt",
                "url": "stellenmarkt"
            },
            {
                "name": "Karriere bei activjob",
                "url": "karriere_activjob"
            },
        ],
    }

    menu_left = menu_items.get(active_node)

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
