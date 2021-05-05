# -*- coding: utf-8 -*-
# from odoo import http


# class RlmFtp(http.Controller):
#     @http.route('/rlm_ftp/rlm_ftp/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/rlm_ftp/rlm_ftp/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('rlm_ftp.listing', {
#             'root': '/rlm_ftp/rlm_ftp',
#             'objects': http.request.env['rlm_ftp.rlm_ftp'].search([]),
#         })

#     @http.route('/rlm_ftp/rlm_ftp/objects/<model("rlm_ftp.rlm_ftp"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('rlm_ftp.object', {
#             'object': obj
#         })
