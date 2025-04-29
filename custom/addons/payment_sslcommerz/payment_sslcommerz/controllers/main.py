from odoo import http
from odoo.http import request
import requests

class SSLCommerzController(http.Controller):

    @http.route('/payment/sslcommerz/initiate', type='http', auth='public', csrf=False, website=True)
    def sslcommerz_initiate(self, **post):
        store_id = post.get('store_id')
        amount = post.get('amount')
        currency = post.get('currency')
        tran_id = post.get('tran_id')

        # Get the password from settings in Odoo
        acquirer = request.env['payment.acquirer'].sudo().search([('provider', '=', 'sslcommerz')], limit=1)
        store_password = acquirer.sslcommerz_store_passwd

        # Prepare the data to send to SSLCommerz
        data = {
            'store_id': store_id,
            'store_passwd': store_password,
            'total_amount': amount,
            'currency': currency,
            'tran_id': tran_id,
            'success_url': request.httprequest.host_url + 'payment/sslcommerz/success',
            'fail_url': request.httprequest.host_url + 'payment/sslcommerz/fail',
            'cancel_url': request.httprequest.host_url + 'payment/sslcommerz/cancel',
            'cus_name': "Customer",
            'cus_email': "customer@example.com",
            'cus_add1': "Dhaka",
            'cus_phone': "01234567890",
        }

        # Send the request to SSLCommerz
        response = requests.post('https://sandbox.sslcommerz.com/gwprocess/v4/api.php', data=data)
        result = response.json()

        # Redirect user to SSLCommerz payment page
        if result.get('status') == 'SUCCESS':
            return request.redirect(result['GatewayPageURL'])
        else:
            return "Payment failed. Reason: " + result.get('failedreason', 'Unknown')
