from odoo import models, fields

class PurchasePriceHistory(models.Model):
    _name = 'purchase.price.history'
    _description = 'Purchase Price History'
    _order = 'date desc, id desc'

    product_tmpl_id = fields.Many2one('product.template', string='Product', required=True, ondelete='cascade')
    partner_id = fields.Many2one('res.partner', string='Supplier', required=True)
    price = fields.Float(string='Price', required=True)
    date = fields.Datetime(string='Date', required=True)
    order_id = fields.Many2one('purchase.order', string='Purchase Order', required=True)