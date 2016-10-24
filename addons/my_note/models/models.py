# -*- coding: utf-8 -*-

from odoo import models, fields, api

class my_note(models.Model):
    _name = 'note.note'
    _inherit = ['note.note']

    name = fields.Char()
    value = fields.Integer()
    value2 = fields.Float(compute="_value_pc", store=True)
    value3 = fields.Text()
    description = fields.Text()

    @api.depends('value')
    def _value_pc(self):
        self.value2 = float(self.value) / 100
