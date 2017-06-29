from django.core.urlresolvers import reverse_lazy

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
                    "url": reverse_lazy(
                        "kompetenzbereiche",
                        args=["arbeitnehmerueberlassung"],
                    ),
                },
                {
                    "name": "Ansprechpartner",
                    "url": reverse_lazy(
                        "ansprechpartner",
                        args=["arbeitnehmerueberlassung"],
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
                    "url": reverse_lazy(
                        "referenzen",
                        args=["personalvermittlung"],
                    ),
                },
                {
                    "name": "Ansprechpartner",
                    "url": reverse_lazy(
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
                    "url": reverse_lazy(
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
            "url": "bewerber_arbeitnehmerueberlassung",
            "sublist": [
                {
                    "name": "Ihre Vorteile",
                    "url": reverse_lazy(
                        "vorteile",
                        args=["zeitarbeit"],
                    ),
                },
                {
                    "name": "Berufsfelder",
                    "url": reverse_lazy(
                        "berufsfelder",
                        args=["zeitarbeit"],
                    ),
                },
                {
                    "name": "Ansprechpartner",
                    "url": reverse_lazy(
                        "ansprechpartner",
                        args=["bewerber/", "arbeitnehmerueberlassung"],
                    ),
                },
                {
                    "name": "Stellenmarkt AÜ",
                    "url": reverse_lazy('stellenmarkt'),
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
                    "url": reverse_lazy(
                        "ansprechpartner",
                        args=["bewerber/", "personalvermittlung"],
                    ),
                },
                {
                    "name": "Stellenmarkt PV",
                    "url": reverse_lazy('stellenmarkt'),
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
                    "url": reverse_lazy(
                        "ansprechpartner",
                        args=["bewerber/", "arbeitsvermittlung"],
                    ),
                },
                {
                    "name": "Stellenmarkt AV",
                    "url": reverse_lazy('stellenmarkt'),
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

def build_main_menu(active_nodes=None):


    for item in menu_top:
        item["active"] = item["url"] == active_nodes.get("top")



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
