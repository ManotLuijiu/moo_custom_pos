import frappe


def after_install():
    # Create Custom POS Page
    if not frappe.db.exists("Page", "moo-custom-pos"):
        frappe.get_doc(
            {
                "doctype": "Page",
                "page_name": "moo-custom-pos",
                "title": "Moo Custom POS",
                "module": "Moo Custom POS",
                "standard": "Yes",
            }
        ).insert()
