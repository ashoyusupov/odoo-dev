from odoo import models, fields, api

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    custom_reference = fields.Char(string='Custom Reference', help='A custom reference for this sale order')

    @api.onchange('custom_reference')
    def _onchange_custom_reference(self):
        if self.custom_reference:
            self.custom_reference = self.custom_reference.upper()