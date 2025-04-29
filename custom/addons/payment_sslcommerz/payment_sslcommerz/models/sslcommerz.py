from odoo import fields, models

class AcquirerSSLCommerz(models.Model):
    _inherit = 'payment.acquirer'

    provider = fields.Selection(selection_add=[('sslcommerz', 'SSLCommerz')])
    sslcommerz_store_id = fields.Char('Store ID')
    sslcommerz_store_passwd = fields.Char('Store Password')
