import frappe

# Sending Data From Other Applications To ERPNext
# refer to sendtoERP.py

@frappe.whitelist()
def receive_data():
	data = frappe.request.data

	print(f"\n\n{data}\n\n")

	return

