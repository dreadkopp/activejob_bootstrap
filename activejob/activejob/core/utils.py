from django.core.urlresolvers import reverse


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
                "url": "unternehmensprofil",
            },
            {
                "name": "Leitbild",
                "url": "leitbild",
            },
            {
                "name": "Standorte",
                "url": "standorte",
            },
            {
                "name": "Kontakt",
                "url": "kontakt",
            },
        ],
        "unternehmen": [
            {
                "name": "Arbeitnehmerüberlassung",
                "url": "arbeitnehmerueberlassung",
                "sublist": [
                    {
                        "name": "Kompetenzbereiche",
                        "url": reverse(
                            "kompetenzbereiche",
                            args=["arbeitnehmerueberlassung"],
                        ),
                    },
                    {
                        "name": "Ansprechpartner",
                        "url": reverse(
                            "ansprechpartner",
                            args=["zeitarbeit"],
                        ),
                    },
                ]
            },
            {
                "name": "Personalvermittlung",
                "url": "personalvermittlung",
                "sublist": [
                    {
                        "name": "Kompetenzbereiche",
                        "url": "kompetenzbereiche",
                    },
                    {
                        "name": "Referenzen",
                        "url": "referenzen",
                    },
                    {
                        "name": "Ansprechpartner",
                        "url": reverse(
                            "ansprechpartner",
                            args=["personalvermittlung"],
                        ),
                    },
                ]
            },
            {
                "name": "Arbeitsvermittlung",
                "url": "arbeitsvermittlung",
                "sublist": [
                    {
                        "name": "Kompetenzbereiche",
                        "url": "kompetenzbereiche",
                    },
                    {
                        "name": "Ansprechpartner",
                        "url": reverse(
                            "ansprechpartner",
                            args=["arbeitsvermittlung"],
                        ),
                    },
                ]
            },
            {
                "name": "Personalanfrage",
                "url": "personalanfrage",
            },
            {
                "name": "Personalauswahl",
                "url": "personalauswahl",
            },
        ],
        "bewerber": [
            {
                "name": "Arbeitnehmerüberlassung",
                "url": "bewerber_zeitarbeit",
                "sublist": [
                    {
                        "name": "Ihre Vorteile",
                        "url": reverse(
                            "vorteile",
                            args=["zeitarbeit"],
                        ),
                    },
                    {
                        "name": "Berufsfelder",
                        "url": reverse(
                            "berufsfelder",
                            args=["zeitarbeit"],
                        ),
                    },
                    {
                        "name": "Ansprechpartner",
                        "url": reverse(
                            "ansprechpartner",
                            args=["zeitarbeit"],
                        ),
                    },
                    {
                        "name": "Stellenmarkt AÜ",
                        "url": reverse("stellenmarkt") + "?aü",
                    },
                ]
            },
            {
                "name": "Personalvermittlung",
                "url": "bewerber_personalvermittlung",
                "sublist": [
                    {
                        "name": "Ihre Vorteile",
                        "url": "vorteile",
                    },
                    {
                        "name": "Berufsfelder",
                        "url": "berufsfelder",
                    },
                    {
                        "name": "Ansprechpartner",
                        "url": reverse(
                            "ansprechpartner",
                            args=["personalvermittlung"],
                        ),
                    },
                    {
                        "name": "Stellenmarkt PV",
                        "url": reverse("stellenmarkt") + "?pv",
                    },
                ]
            },
            {
                "name": "Arbeitsvermittlung",
                "url": "bewerber_arbeitsvermittlung",
                "sublist": [
                    {
                        "name": "Ihre Vorteile",
                        "url": "vorteile",
                    },
                    {
                        "name": "Berufsfelder",
                        "url": "berufsfelder",
                    },
                    {
                        "name": "Fragen und Antworten",
                        "url": "bewerber_arbeitsvermittlung_antworten",
                    },
                    {
                        "name": "Ansprechpartner",
                        "url": reverse(
                            "ansprechpartner",
                            args=["arbeitsvermittlung"],
                        ),
                    },
                    {
                        "name": "Stellenmarkt AV",
                        "url": reverse("stellenmarkt") + "?av",
                    },
                ]
            },
            {
                "name": "Karriereberatung",
                "url": "karriereberatung",
            },
            {
                "name": "Stellenmarkt",
                "url": "stellenmarkt",
            },
            {
                "name": "Karriere bei activjob",
                "url": "karriere_activjob",
            },
        ],
    }

    menu_left = menu_items.get(active_nodes.get("top"), [])

    for item in menu_left:
        item["active"] = item["url"] == active_nodes.get("left")
        if "sublist" in item:
            for subitem in item["sublist"]:
                subitem["active"] = subitem["name"] == active_nodes.get("sub")

    return {
        "menu_top": menu_top,
        "menu_left": menu_left,
    }
