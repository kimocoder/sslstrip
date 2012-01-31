# Copyright (c) 2004-2009 Moxie Marlinspike
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
from sslstrip.DummyResponseTamperer import DummyResponseTamperer

class AppCachePoison(DummyResponseTamperer):

    '''
    AppCachePosion performs HTML5 AppCache poisioning attack
    '''
    def __init__(self, config):
        self.config = config
        logging.log(logging.DEBUG, "Tampering enabled.")

    def tamper(self, url, data, headers, req_headers):
        if not self.isEnabled():
          return data
          
        

        # headers manipulation - see http://twistedmatrix.com/documents/10.1.0/api/twisted.web.http_headers.Headers.html
        # setting headers
        #headers.setRawHeaders("X-aaa", ["aaa"])
        # getting headers
        #headers.getRawHeaders("Content-Type")

        return data+repr(self.config)

