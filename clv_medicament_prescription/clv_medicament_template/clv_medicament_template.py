# -*- encoding: utf-8 -*-
################################################################################
#                                                                              #
# Copyright (C) 2013-Today  Carlos Eduardo Vercelino - CLVsol                  #
#                                                                              #
# This program is free software: you can redistribute it and/or modify         #
# it under the terms of the GNU Affero General Public License as published by  #
# the Free Software Foundation, either version 3 of the License, or            #
# (at your option) any later version.                                          #
#                                                                              #
# This program is distributed in the hope that it will be useful,              #
# but WITHOUT ANY WARRANTY; without even the implied warranty of               #
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the                #
# GNU Affero General Public License for more details.                          #
#                                                                              #
# You should have received a copy of the GNU Affero General Public License     #
# along with this program.  If not, see <http://www.gnu.org/licenses/>.        #
################################################################################

from openerp.osv import fields, osv

class clv_medicament_template(osv.osv):
    _inherit = 'clv_medicament.template'

    _columns = {
        'prescription_id': fields.many2one('clv_medicament_prescription',
                                            string='Prescription', ),
        }

class clv_medicament_prescription(osv.osv):
    _inherit = 'clv_medicament_prescription'

    _columns = {
        'prescription_lines': fields.one2many('clv_medicament.template',
                                              'prescription_id',
                                              string='Prescription lines',),
    }

