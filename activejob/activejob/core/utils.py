from .sitemenu import menu_top, menu_items


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
