from odoo import http
from odoo.http import request

class SSLCommerzController(http.Controller):

    @http.route('/payment/sslcommerz/return', type='http', auth='public', csrf=False)
    def sslcommerz_return(self, **post):
        txn_id = post.get('tran_id')
        status = post.get('status')
        
        tx = request.env['payment.transaction'].sudo().search([('reference', '=', txn_id)], limit=1)
        
        if tx and status == 'VALID':
            tx._set_transaction_done()
        else:
            tx._set_transaction_cancel()

        return request.redirect('/payment/status')
