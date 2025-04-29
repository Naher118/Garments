from odoo import models, fields

class PaymentAcquirerSSLCommerz(models.Model):
    _name = 'sslcommerz.payment.acquirer'
    _description = 'SSLCommerz Acquirer Settings'

    name = fields.Char('Name', required=True)
    store_id = fields.Char('Store ID', required=True)
    store_passwd = fields.Char('Store Password', required=True)
    sandbox_mode = fields.Boolean('Use Sandbox Mode', default=True)
