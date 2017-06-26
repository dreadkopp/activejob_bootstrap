def build_main_menu(active_nodes=None):
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
        item["active"] = item["url"] == active_nodes.get("top")

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
                "url": "bewerber_zeitarbeit"
            },
            {
                "name": "Personalvermittlung",
                "url": "bewerber_personalvermittlung"
            },
            {
                "name": "Arbeitsvermittlung",
                "url": "bewerber_arbeitsvermittlung"
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

    menu_left = menu_items.get(active_nodes.get("top"), [])

    for item in menu_left:
        item["active"] = item["url"] == active_nodes.get("left")

    return {
        "menu_top": menu_top,
        "menu_left": menu_left,
    }


class MenuMixin:
    active_nodes = {pos: None for pos in ["top", "left", "sub"]}

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        menu_context = build_main_menu(
            active_nodes=self.active_nodes,
        )
        context.update(menu_context)
        return context
