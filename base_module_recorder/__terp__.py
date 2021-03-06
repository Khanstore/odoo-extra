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
    'name': 'Module Recorder create a new module without any development',
    'version': '1.0',
    'category': 'Generic Modules/Base',
    'description': """
This module allows you to create a new module without any development.
It records all operations on objects during the recording session and
produce a .ZIP module. So you can create your own module directly from
the Open ERP client.

This version works for creating and updating existing records. It recomputes
dependencies and links for all types of widgets (many2one, many2many, ...).
It also support workflows and demo/update data.

This should help you to easily create reusable and publishable modules
for custom configurations and demo/testing data.

How to use it:
1. Start the recording
2. Do stuff in your Open ERP client
3. Stop the recording session
4. Export to a reusable module
    """,
    'author': 'Tiny',
    'website': 'http://www.openerp.com',
    'depends': ['base','base_module_record'],
    'init_xml': [],
    'update_xml': ['base_module_recorder_wizard.xml'],
    'demo_xml': [],
    'installable': True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
