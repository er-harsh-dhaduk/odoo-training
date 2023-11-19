from odoo import http


class POSRpcCallExample(http.Controller):

    @http.route("/pos/rpc/example", auth="user", type="json")
    def pos_example(self, **kwargs):
        result = http.request.env['res.lang'].search_read([])
        return result
