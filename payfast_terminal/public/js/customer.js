frappe.ui.form.on('Customer', {
    refresh: function(frm) {
        frm.add_custom_button(__('Tokenize Card'), function() {
            frappe.prompt(
                [
                    {
                        "fieldname": "card_number",
                        "label": __("Card Number"),
                        "fieldtype": "Data",
                        "reqd": 1
                    },
                    {
                        "fieldname": "expiry_month",
                        "label": __("Expiry Month"),
                        "fieldtype": "Data",
                        "reqd": 1
                    },
                    {
                        "fieldname": "expiry_year",
                        "label": __("Expiry Year"),
                        "fieldtype": "Data",
                        "reqd": 1
                    },
                    {
                        "fieldname": "cvv",
                        "label": __("CVV"),
                        "fieldtype": "Data",
                        "reqd": 1
                    }
                ],
                function(data) {
                    frappe.call({
                        method: "_terminal.api.tokenize_card",
                        args: {
                            customer: frm.doc.name,
                            card_details: data
                        },
                        callback: function(r) {
                            if (r.message) {
                                frappe.msgprint(__("Card tokenized successfully"));
                                frm.reload_doc();
                            }
                        }
                    });
                },
                __("Enter Card Details")
            );
        });
    }
});
