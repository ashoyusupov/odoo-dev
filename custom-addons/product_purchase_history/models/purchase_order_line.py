from odoo import models, api

class PurchaseOrderLine(models.Model):
    _inherit = 'purchase.order.line'

    @api.model
    def create(self, vals):
        res = super(PurchaseOrderLine, self).create(vals)
        if res.product_id and res.price_unit:
            self.env['purchase.price.history'].create({
                'product_tmpl_id': res.product_id.product_tmpl_id.id,
                'partner_id': res.order_id.partner_id.id,
                'price': res.price_unit,
                'date': res.order_id.date_order,
                'order_id': res.order_id.id,
            })
        return res

    def write(self, vals):
        res = super(PurchaseOrderLine, self).write(vals)
        if 'price_unit' in vals:
            for line in self:
                self.env['purchase.price.history'].create({
                    'product_tmpl_id': line.product_id.product_tmpl_id.id,
                    'partner_id': line.order_id.partner_id.id,
                    'price': line.price_unit,
                    'date': line.order_id.date_order,
                    'order_id': line.order_id.id,
                })
        return res