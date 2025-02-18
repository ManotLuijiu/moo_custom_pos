import frappe
from frappe import _

@frappe.whitelist()
def get_items(pos_profile=None):
    """Get items with unit conversion details"""
    items = frappe.get_all(
        'Item',
        fields=['name', 'item_code', 'item_name', 'stock_uom', 'rate'],
        filters={'is_sales_item': 1}
    )

    for item in items:
        # Get unit conversions
        uoms = frappe.get_all(
            'UOM Conversion Detail',
            filters={'parent': item.item_code},
            fields=['uom', 'conversion_factor']
        )
        item.unit_conversions = uoms
    
    return items

@frappe.whitelist()
def create_pos_invoice(data):
    """Create POS Invoice with unit conversions"""
    try:
        data = frappe.parse_json(data)
        doc = frappe.new_doc('POS Invoice')
        # Set invoice fields
        doc.update(data)
        doc.insert()
        return doc
    except Exception as e:
        frappe.throw(_("Error creating POS Invoice: {0}").format(str(e)))