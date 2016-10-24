# -*- coding: utf-8 -*-
from odoo import http

class MyNote(http.Controller):
    @http.route('/my_note/my_note/', auth='public')
    def index(self, **kw):
        return "Hello, world"

    @http.route('/my_note/my_note/objects/', auth='public')
    def list(self, **kw):
        return http.request.render('my_note.listing', {
            'root': '/my_note/my_note',
            'objects': http.request.env['my_note.my_note'].search([]),
        })

    @http.route('/my_note/my_note/objects/<model("my_note.my_note"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('my_note.object', {
            'object': obj
        })
