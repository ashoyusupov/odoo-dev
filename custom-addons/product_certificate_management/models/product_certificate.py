from odoo import models, fields, api
from datetime import datetime, timedelta

class ProductCertificate(models.Model):
    _name = 'product.certificate'
    _description = 'Product Certificate'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    product_id = fields.Many2one('product.product', string='Product', required=True)
    certificate = fields.Char(string='Certificate', required=True)
    responsible_user_id = fields.Many2one('res.users', string='Responsible User', required=True)
    start_date = fields.Date(string='Certificate Start Date', required=True)
    end_date = fields.Date(string='Certificate End Date', required=True)
    days_before_expiry = fields.Integer(string='Days Before Expiry', compute='_compute_days_before_expiry', store=True)

    @api.depends('end_date')
    def _compute_days_before_expiry(self):
        today = fields.Date.today()
        for record in self:
            if record.end_date:
                delta = record.end_date - today
                record.days_before_expiry = delta.days
            else:
                record.days_before_expiry = 0

    @api.model
    def _cron_check_certificate_expiry(self):
        certificates = self.search([
            ('end_date', '=', fields.Date.to_string(fields.Date.today() + timedelta(days=10)))
        ])
        mail_template = self.env.ref('product_certificate_management.mail_template_certificate_expiry')
        for certificate in certificates:
            mail_template.send_mail(certificate.id, force_send=True)