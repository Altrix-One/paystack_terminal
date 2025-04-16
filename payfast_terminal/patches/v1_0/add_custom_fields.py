import frappe
from frappe.custom.doctype.custom_field.custom_field import create_custom_fields

def execute():
    """Add custom fields for Payfast Terminal"""
    custom_fields = {
        "Sales Invoice": [
            {
                "fieldname": "terminal_reference",
                "label": "Terminal Reference",
                "fieldtype": "Data",
                "insert_after": "payment_schedule",
                "read_only": 1,
                "no_copy": 1,
                "print_hide": 1
            },
            {
                "fieldname": "payfast_status",
                "label": "Payfast Status",
                "fieldtype": "Data",
                "insert_after": "terminal_reference",
                "read_only": 1,
                "no_copy": 1,
                "print_hide": 1
            },
            {
                "fieldname": "recurring_payment",
                "label": "Recurring Payment",
                "fieldtype": "Check",
                "insert_after": "payfast_status",
                "read_only": 0,
                "no_copy": 0,
                "print_hide": 0
            },
             {
                "fieldname": "recurring_interval",
                "label": "Recurring Interval",
                "fieldtype": "Select",
                "options": "Daily\nWeekly\nMonthly\nYearly",
                "insert_after": "recurring_payment",
                "read_only": 0,
                "no_copy": 0,
                "print_hide": 0
            }
        ],
        "Customer": [
            {
                "fieldname": "payfast_customer_code",
                "label": "Payfast Customer Code",
                "fieldtype": "Data",
                "insert_after": "customer_details",
                "read_only": 1,
                "no_copy": 1,
                "print_hide": 1
            },
            {
                "fieldname": "payfast_token",
                "label": "Payfast Token",
                "fieldtype": "Data",
                "insert_after": "payfast_customer_code",
                "read_only": 1,
                "no_copy": 1,
                "print_hide": 1
            }
        ],
        "Payment Entry": [
            {
                "fieldname": "payfast_reference",
                "label": "Payfast Reference",
                "fieldtype": "Data",
                "insert_after": "reference_no",
                "read_only": 1,
                "no_copy": 1,
                "print_hide": 1
            }
        ]
    }
    
    create_custom_fields(custom_fields)
