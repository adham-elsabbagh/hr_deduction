# -*- coding: utf-8 -*-

from odoo import models, fields, api,_
from datetime import datetime


class hr_deduction(models.Model):
    _name = 'hr.deduction'
    _inherit = 'hr.payslip'


    employee_id = fields.Many2one('hr.employee', string='Employee', required=True, readonly=False)
    ded_date = fields.Date(string="Date", required=True, )
    ded_val = fields.Float(string="Deduction Value",  required=True, )
    note = fields.Text(string="Note", required=False, )
    code = fields.Char(string="code", required=False, )
    state_last_update = fields.Datetime(required=False, )
    state = fields.Selection(string="State", selection=[('draft', 'Draft'), ('confirm', 'Confirmed'), ], required=False, )


    @api.model
    def create(self, values):
        values['code'] = self.env['ir.sequence'].next_by_code('hr.deduction') or 'New'
        return super(hr_deduction, self).create(values)


    @api.multi
    def action_confirm(self):
        for record in self:
            record.write({
                'state': 'confirm',
                'state_last_update': datetime.now()
            })



class hr_employee(models.Model):
    _inherit = 'hr.employee'


    @api.model
    def deduction_compute(self, employee, date_from,date_to):
        total = 0
        deduction_ids = self.env['hr.deduction'].search(
            [('employee_id', '=', employee), ('date', '>=', date_from),
             ('date', '<=', date_to), ('state', '=', 'confirm')])
        for record in deduction_ids:
            total += record.ded_val
        return total




