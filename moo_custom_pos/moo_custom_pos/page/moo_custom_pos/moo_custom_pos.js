frappe.pages['moo-custom-pos'].on_page_load = function(wrapper) {
	var page = frappe.ui.make_app_page({
		parent: wrapper,
		title: 'Moo Custom POS',
		single_column: true
	});
}