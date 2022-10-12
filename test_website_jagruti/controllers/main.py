import requests
from odoo import http
from odoo.http import request
import werkzeug


class DoctorsD(http.Controller):

    @http.route('/doctors/details/form', auth='public',type='http',website=True)
    def doctor_get(self, **kw):
        if not request.session.uid:
            return werkzeug.utils.redirect('/web/login', 303)
        doctor_ids = request.env['doctor.doctor'].search([])
        values = {'doctors':doctor_ids}
        return request.render("test_website_jagruti.doctors_display", values)

    @http.route(['/doctors/form'], type='http', auth="public", website=True)
    def doctors_form(self, **post):
        return request.render("test_website_jagruti.doctors_reg", {})

    @http.route(['/doctors/form/submit'], type='http', auth="public", website=True)
    def appoinment_form_submit(self, **post):
        
        doctor_id = request.env['doctor.doctor'].sudo().create({
            'name': post.get('name'),
            'mobile': post.get('mobile'),
            'city':post.get('city'),
            'email':post.get('email'),
        })
        vals = {
                'doctor_id':doctor_id
                }
        return request.render("test_website_jagruti.doctor_form_success", vals)
