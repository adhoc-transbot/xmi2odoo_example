# -*- coding: utf-8 -*-
from openerp import models, fields, api, _
from openerp.exceptions import Warning


class course(models.Model):
    """"""

    _name = 'openacademy.course'
    _description = 'course'

    name = fields.Char(
        string='Name',
        required=True
        )
    description = fields.Text(
        string='Description'
        )
    responsible_id = fields.Many2one(
        'res.users',
        string='Responsible'
        )
    session_ids = fields.One2many(
        'openacademy.session',
        'course_id',
        string='session_ids'
        )
     = fields.Many2many(
        'res.partner',
        'openacademy_____rel',
        'course_id',
        'partner_id',
        string='<no label>'
        )

    _constraints = [
    ]

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4: