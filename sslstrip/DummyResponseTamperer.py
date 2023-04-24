# Copyright (c) 2004-2009 Moxie Marlinspike, Krzysztof Kotowicz
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 59 Temple Place, Suite 330, Boston, MA 02111-1307
# USA
#

import logging
from sslstrip.URLMonitor import URLMonitor

class DummyResponseTamperer:

    '''
    DummyResponseTamperer is an exemplary class for server response tampering.
    '''

    def __init__(self, config):
        self.config = config
        self.urlMonitor = URLMonitor.getInstance()
        logging.log(logging.DEBUG, "Tampering enabled.")

    def isEnabled(self):
        return self.config["enabled"]

    def tamper(self, url, data, headers, req_headers, ip):
        return data if self.isEnabled() else data

