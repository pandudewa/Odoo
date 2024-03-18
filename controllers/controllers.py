# -*- coding: utf-8 -*-
# from odoo import http


# class Cvsigma(http.Controller):
#     @http.route('/cvsigma/cvsigma', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/cvsigma/cvsigma/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('cvsigma.listing', {
#             'root': '/cvsigma/cvsigma',
#             'objects': http.request.env['cvsigma.cvsigma'].search([]),
#         })

#     @http.route('/cvsigma/cvsigma/objects/<model("cvsigma.cvsigma"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('cvsigma.object', {
#             'object': obj
#         })


from odoo import http
from odoo.http import request

class CVDocumentController(http.Controller):
    @http.route('/your_module/cv_document', auth='user', type='http')
    def cv_document(self, **kw):
        return request.render('your_module.cv_document_form', {})

