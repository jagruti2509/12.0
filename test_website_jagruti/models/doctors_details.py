from odoo import models,fields,api, _
from datetime import datetime
from odoo.tools import DEFAULT_SERVER_DATETIME_FORMAT, DEFAULT_SERVER_DATE_FORMAT


class DoctorsDoctors(models.Model):
    _name = 'doctor.doctor'
    description='Doctors'

    name = fields.Char(string='Name')
    docotor_speciality = fields.Selection(
        [('cardiologist','Cardiologist'),('dentist','Dentist'),('orthopaedic','Orthopaedic'),
        ('neurologist','Neurologist'),('gynecologist','Gynecologist'),('general','General')],
        string="Speciality")
    mobile = fields.Char(string='mobile')
    email = fields.Char(string="Email")
    city = fields.Char("City")
    state_id = fields.Many2one("res.country.state", string='State', ondelete='restrict', domain="[('country_id', '=?', country_id)]")
    country_id = fields.Many2one('res.country', string='Country')
    image = fields.Binary(
        "Image", attachment=True,
        help="This field holds the image used for this provider, limited to 1024x1024px")
    image_medium = fields.Binary(
        "Medium-sized image", attachment=True,
        help="Medium-sized image of this provider. It is automatically "
             "resized as a 128x128px image, with aspect ratio preserved. "
             "Use this field in form views or some kanban views.")
    image_small = fields.Binary(
        "Small-sized image", attachment=True,
        help="Small-sized image of this provider. It is automatically "
             "resized as a 64x64px image, with aspect ratio preserved. "
             "Use this field anywhere a small image is required.")
