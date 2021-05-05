#-*- coding: utf-8 -*-

from odoo import models, fields, api


class rlm_ftp(models.Model):
    _name = 'rlm_ftp.rlm_ftp'
    _description = 'rlm_ftp.rlm_ftp'
    
    datas=fields.Many2many('ir.attachment')
    name=fields.Char(string="name")

    @api.model
    def schedule_download(self):
        attachment_obj = self.env['ir.attachment']
        with request.urlopen('ftp://ftp.dlink.eu/Manuals/DES-1008PA_Manual.pdf') as response:
            attachment_obj.create({'name': 'DES-1008PA_Manual.pdf', 'datas': response.read()})


