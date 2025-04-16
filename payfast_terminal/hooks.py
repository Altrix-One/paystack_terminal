"""
Author:Hedgar Ajakaiye
Date: January 02, 2025
Description: A custom module for integrating Payfast Terminal with ERPNext
"""

app_name = "payfast_terminal"
app_title = "Payfast Terminal"
app_publisher = "Gemutanalytics"
app_description = "Payfast Terminal Integration for ERPNext Healthcare"
app_email = "dev@gemutanalytics.com"
app_license = "MIT"

# DocTypes to be registered
doctype_list = ["Payfast Settings"]

# Module configuration
modules = {
    "Payfast Terminal": {
        "color": "#25c16f",
        "icon": "octicon octicon-credit-card",
        "type": "module",
        "label": "Payfast Terminal",
        "category": "Modules"
    }
}

# include js, css files in header of desk.html
app_include_js = [
    "/assets/payfast_terminal/js/payfast_terminal.js",
    "/assets/payfast_terminal/js/customer.js"
]

# Doc Events
doc_events = {
    "Payment Entry": {
        "on_submit": "payfast_terminal.api.update_payment_status"
    }
}

# Custom fields to be created
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["name", "in", [
                "Customer-paystack_customer_code",
                "Payment Entry-payfast_reference",
                "Sales Invoice-terminal_reference",
                "Sales Invoice-payfast_status"
            ]]
        ]
    },
    {
        "dt": "DocType",
        "filters": [["name", "in", ["Payfast Settings"]]]
    },
    {
        "dt": "Mode of Payment",
        "filters": [["name", "=", "Payfast Terminal"]],
        "records": [{
            "doctype": "Mode of Payment",
            "mode_of_payment": "Payfast Terminal",
            "type": "Bank",
            "enabled": 1
        }]
    }
]

# DocType JS
doctype_js = {
    "Sales Invoice": "public/js/sales_invoice.js"
}

# Webhooks
webhooks = [
    {
        "webhook": "Payfast Terminal Webhook",
        "url": "/api/method/payfast_terminal.api.handle_webhook",
        "request_method": "POST"
    }
]

# Schedule Tasks for reconciliation
scheduler_events = {
    "daily": [
        "payfast_terminal.api.reconcile_pending_payments",
        "payfast_terminal.api.create_recurring_invoices"
    ]
}
