from odoo import models, fields

class Pendidikan(models.Model):
    _name = 'cnt_testing.pendidikan'
    _description = 'Model untuk data pendidikan'

    name = fields.Char(string='Nama', required=True)
    deskripsi = fields.Text(string='Deskripsi')
