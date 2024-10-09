from odoo import models, fields, api

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    last_purchase_price = fields.Float(string='Last Purchase Price', compute='_compute_last_purchase_price', store=True)
    purchase_price_history_ids = fields.One2many('purchase.price.history', 'product_tmpl_id', string='Purchase Price History')

    @api.depends('purchase_price_history_ids', 'purchase_price_history_ids.price')
    def _compute_last_purchase_price(self):
        for product in self:
            last_history = product.purchase_price_history_ids.sorted(key=lambda r: r.date, reverse=True)
            product.last_purchase_price = last_history[0].price if last_history else 0.0