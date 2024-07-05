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
        ('other', 'Other'),
    ], string='Jenis_Kelamin')
    sd = fields.Boolean(string='SD')
    smp = fields.Boolean(string='SMP')
    sma = fields.Boolean(string='SMA')
    sltp = fields.Boolean(string='SLTP')
    smk = fields.Boolean(string='SMK')
    smu = fields.Boolean(string='SMU')
    slta = fields.Boolean(string='SLTA')
    kuliah = fields.Boolean(string='KULIAH')
    