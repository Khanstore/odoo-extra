##############################################################################
#
# Copyright (c) 2004 TINY SPRL. (http://tiny.be) All Rights Reserved.
#                    Fabien Pinckaers <fp@tiny.Be>
#
# WARNING: This program as such is intended to be used by professional
# programmers who take the whole responsability of assessing all potential
# consequences resulting from its eventual inadequacies and bugs
# End users who are looking for a ready-to-use solution with commercial
# garantees and support are strongly adviced to contract a Free Software
# Service Company
#
# This program is Free Software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place - Suite 330, Boston, MA  02111-1307, USA.
#
##############################################################################

from datetime import date,timedelta
import time
from osv import fields, osv
from datetime import datetime

class project_project(osv.osv):
    _inherit = 'project.project'
    _description = 'project.project'

    def write(self, cr, uid, ids,vals, *args, **kwargs):
        if 'date_end' in vals and vals['date_end']:
            data_project = self.browse(cr,uid,ids)
            for prj in data_project:
                c= date(*time.strptime(vals['date_end'],'%Y-%m-%d')[:3])
                if prj.date_end:
                    d= date(*time.strptime(prj.date_end,'%Y-%m-%d')[:3])
                    for task in prj.tasks:
                        if task.date_deadline:
                            f = (datetime(*time.strptime(task.date_deadline,'%Y-%m-%d  %H:%M:%S')[:6])+(c-d)).strftime('%Y-%m-%d %H:%M:%S')
                            self.pool.get('project.task').write(cr,uid,task.id,{'date_deadline':f})
        return super(project_project,self).write(cr, uid, ids,vals, *args, **kwargs)

project_project()