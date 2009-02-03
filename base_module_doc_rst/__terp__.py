# -*- encoding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>). All Rights Reserved
#    $Id$
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Module Technical Guide in Restructured Text ',
    'version': '1.0',
    'category': 'Generic Modules/Base',
    'description': """
    * This module generate the Technical Guides of selected modules in Restructured Text format (RST)
    * It uses the Sphinx (http://sphinx.pocoo.org) implementation of RST
    * It creates a tarball (.tgz file suffix) containing an index file and one file per module
    """,
    'author': 'Tiny',
    'website': 'http://www.openerp.com',
    'depends': ['base'],
    'init_xml': [],
    'update_xml': ['base_module_doc_rst_wizard.xml'],
    'demo_xml': [],
    'installable': True,
    'certificate': '',
}
