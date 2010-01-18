# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.     
#
##############################################################################

{
    'name': 'Integrated Document Management System using paramiko lib',
    'version': '1.0',
    'category': 'Generic Modules/Others',
    'description': """This is a document management system using paramiko lib:
    * SFTP protocoll 
    
""",
    'author': 'Tiny',
    'website': 'http://www.openerp.com',
    'depends': ['base', 'document'],
    'init_xml': [],
    'update_xml': ['document_view.xml','security/ir.model.access.csv'],
    'demo_xml': [],
    'installable': True,
    'active': False,    
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
