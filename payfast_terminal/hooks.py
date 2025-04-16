"""
Author:Christiaan Swart
Date: January 02, 2025
Description: A custom module for integrating  Terminal with ERPNext
"""

app_name = "_terminal"
app_title = " Terminal"
app_publisher = "Gemutanalytics"
app_description = " Terminal Integration for ERPNext"
app_email = "info@cohenix.com"
app_license = "MIT"

# DocTypes to be registered
doctype_list = [" Settings"]

# Module configuration
modules = {
    " Terminal": {
        "color": "#25c16f",
        "icon": "octicon octicon-credit-card",
        "type": "module",
        "label": " Terminal",
        "category": "Modules"
    }
}

# include js, css files in header of desk.html
app_include_js = [
    "/assets/_terminal/js/_terminal.js",
    "/assets/_terminal/js/customer.js"
]

# Doc Events
doc_events = {
    "Payment Entry": {
        "on_submit": "_terminal.api.update_payment_status"
    }
}

# Custom fields to be created
fixtures = [
    {
        "dt": "Custom Field",
        "filters": [
            ["name", "in", [
                "Customer-paystack_customer_code",
                "Payment Entry-_reference",
                "Sales Invoice-terminal_reference",
                "Sales Invoice-_status"
            ]]
        ]
    },
    {
        "dt": "DocType",
        "filters": [["name", "in", [" Settings"]]]
    },
    {
        "dt": "Mode of Payment",
        "filters": [["name", "=", " Terminal"]],
        "records": [{
            "doctype": "Mode of Payment",
            "mode_of_payment": " Terminal",
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
        "webhook": " Terminal Webhook",
        "url": "/api/method/_terminal.api.handle_webhook",
        "request_method": "POST"
    }
]

# Schedule Tasks for reconciliation
scheduler_events = {
    "daily": [
        "_terminal.api.reconcile_pending_payments",
        "_terminal.api.create_recurring_invoices"
    ]
}
