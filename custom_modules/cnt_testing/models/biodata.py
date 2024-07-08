from odoo import models, fields

class Biodata(models.Model):
    _name = "cnt_testing.biodata"

    name = fields.Char(string="Nama")
    fullname = fields.Char(string="Nama Lengkap")
    tanggal_lahir = fields.Date(string="Tanggal Lahir")
    umur = fields.Integer(string="Umur")
    anak = fields.Integer(string="Anak")
    foto = fields.Binary(string="Foto")
    jenis_kelamin = fields.Selection([
        ('laki-laki', 'Laki-laki'),
        ('perempuan', 'Perempuan'),
    ], string='Jenis_Kelamin')

    pendidikan_ids = fields.Many2many('cnt_testing.pendidikan', string='Pendidikan')

    