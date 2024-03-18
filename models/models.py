# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError
import re

class Print(models.Model):
    _name = "print.model"

    name = fields.Char()

    def print(self):
        for record in self:
            record.name = "print"
        return True

class Cv(models.Model):
    _name = 'cv.model'
    _description = 'cv.model'

    name = fields.Char(required=True)
    email = fields.Char(string='Email', validate='_check_valid_email', required=True)
    phone = fields.Char(required=True, default='+62')
    address = fields.Text(required=True)
    linkedin_link = fields.Char(string='LinkedIn Url Link', validate='_check_valid_linkedin_link')
    instagram_link = fields.Char(string='Instagram Url Link', validate='_check_valid_instagram_link')
    photo = fields.Binary(string='Photo', attachment=True, required=True)
    aspiration = fields.Text(string='Aspiration', required=True)
    business_unit = fields.Many2one(comodel_name='unit.model', inverse_name='id_cv', string='Business Unit')
    self_description = fields.Text(string='Self Description', required=True)
    position = fields.Char(String='Position', required=True)
    education = fields.One2many(comodel_name='education.model', inverse_name='id_cv', string='Education History')
    qualification = fields.One2many(comodel_name='qualification.model', inverse_name='id_cv', string='Professional Qualification')
    experience = fields.One2many(comodel_name='experience.model', inverse_name='id_cv', string='Working Experience')
    language = fields.One2many(comodel_name='language.model', inverse_name='id_cv', string='Language')


    @api.constrains('email')
    def _check_valid_email(self):
        for record in self:
            if record.email:
                if not re.match(r"[^@]+@[^@]+\.[^@]+", record.email):
                    raise ValidationError("Email must be a valid email address.")

    @api.constrains('linkedin_link')
    def _check_valid_linkedin_link(self):
        for record in self:
            if record.linkedin_link and not record.linkedin_link.startswith(('http://', 'https://')):
                raise ValidationError("LinkedIn link must start with 'http://' or 'https://'.")

    @api.constrains('instagram_link')
    def _check_valid_instagram_link(self):
        for record in self:
            if record.instagram_link and not record.instagram_link.startswith(('http://', 'https://')):
                raise ValidationError("Instagram link must start with 'http://' or 'https://'.")

    @api.constrains('photo')
    def _check_valid_photo(self):
        for record in self:
            if record.photo:
                # allowed_extensions = ['jpg', 'jpeg', 'png']
                # if not record.photo.filename.lower().endswith(tuple(allowed_extensions)):
                #     raise ValidationError("Invalid photo format. Supported formats: JPG, JPEG, PNG.")

                max_size_mb = 5
                max_size_bytes = max_size_mb * 1024 * 1024
                if len(record.photo) > max_size_bytes:
                    raise ValidationError(f"Photo size exceeds the maximum allowed size of {max_size_mb} MB.")

class Education(models.Model):
    _name = 'education.model'

    degree = fields.Char(string='Degree', required=True)
    school = fields.Char(string='School/University', required=True)
    year = fields.Char(string='Year', required=True)
    id_cv = fields.Many2one(comodel_name='cv.model', string='CV', ondelete='cascade')

class Qualification(models.Model):
    _name = 'qualification.model'

    description = fields.Html(string='Description', required=True)
    id_cv = fields.Many2one(comodel_name='cv.model', string='CV', ondelete='cascade')

class Experience(models.Model):
    _name = 'experience.model'
    _rec_name = 'company_name'

    company_name = fields.Char(string='Company Name', required=True)
    job_title = fields.Char(string='Job Title', required=True)
    start_date = fields.Date(string='Start Date', required=True)
    end_date = fields.Date(string='End Date', required=True)
    specialization = fields.Char(string='Specialization', required=True)
    role = fields.Char(string='Role', required=True)
    skills = fields.Char(string='Skills', required=True)
    achievement = fields.Char(string='Achievement', required=True)
    description = fields.Html(string='Description', required=True)
    id_cv = fields.Many2one(comodel_name='cv.model', string='CV', ondelete='cascade')

class Unit(models.Model):
    _name = 'unit.model'

    name = fields.Char(string='Business Unit Name', required=True)
    id_cv = fields.Many2one(comodel_name='cv.model', string='CV', ondelete='cascade')

class Language(models.Model):
    _name = 'language.model'

    language = fields.Char(string='Language', required=True)
    spoken = fields.Char(string='Spoken', required=True)
    written = fields.Char(string='Written', required=True)
    id_cv = fields.Many2one(comodel_name='cv.model', string='CV', ondelete='cascade')