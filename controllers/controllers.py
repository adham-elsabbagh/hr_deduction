# -*- coding: utf-8 -*-
from odoo import http

# class HrDeduction(http.Controller):
#     @http.route('/hr_deduction/hr_deduction/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hr_deduction/hr_deduction/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hr_deduction.listing', {
#             'root': '/hr_deduction/hr_deduction',
#             'objects': http.request.env['hr_deduction.hr_deduction'].search([]),
#         })

#     @http.route('/hr_deduction/hr_deduction/objects/<model("hr_deduction.hr_deduction"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hr_deduction.object', {
#             'object': obj
#         })