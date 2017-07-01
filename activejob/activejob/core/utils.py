from .sitemenu import menu_top, menu_items
#DEBUG
import sys

def build_main_menu(active_nodes=None):
    for item in menu_top:
        item["active"] = item["url"] == active_nodes.get("top")

    menu_left = menu_items.get(active_nodes.get("top"), [])

    for item in menu_left:
        item["active"] = item["url"] == active_nodes.get("left")
        if "sublist" in item:
            for subitem in item["sublist"]:
                subitem["active"] = subitem["name"] == active_nodes.get("sub")
                #need to do this here. if this happens in sitemenu.menu_items
                #it tries to resolve reverse_lazy() to early and rises error
                if subitem["name"] == "Stellenmarkt AÜ":
                    subitem["url"] += "?aü"
                if subitem["name"] == "Stellenmarkt PV":
                    subitem["url"] += "?pv"
                if subitem["name"] == "Stellenmarkt AV":
                    subitem["url"] += "?av"
                    #DEBUG
                    subitem["url"] += str(len(menu_left))


    return {
        "menu_top": menu_top,
        "menu_left": menu_left,
    }
