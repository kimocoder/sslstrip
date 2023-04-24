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

import logging, ConfigParser

class ResponseTampererFactory:

    '''
    ResponseTampererFactory creates response tamperer that modifies responses to clients based on config file setting.
    '''

    _instance          = None

    _default_config = {"enabled": False, "tamper_class": "sslstrip.DummyResponseTamperer"}

    def __init__(self):
        pass

    def createTamperer(self):
        logging.log(logging.DEBUG, f"Reading tamper config file: {self}")
        config = ResponseTampererFactory._default_config.copy()
        if self:
            config.update(ResponseTampererFactory.parseConfig(self))
        if config['enabled']:
            logging.log(logging.DEBUG, f'Loading tamper class: {config["tamper_class"]}')
            m = __import__(config["tamper_class"], globals(), locals(), config["tamper_class"])
            return getattr(m, m.__name__.replace(f"{m.__package__}.", ''))(config)

    def parseConfig(self):
        config = ConfigParser.ConfigParser()
        config.read(self)
        readConfig = config._sections
        readConfig.update(config.defaults())
        return readConfig

    def getTampererInstance():
        return ResponseTampererFactory._instance

    def buildTamperer(self):
        if ResponseTampererFactory._instance is None:
            ResponseTampererFactory._instance = (
                ResponseTampererFactory.createTamperer(self)
            )

    getTampererInstance = staticmethod(getTampererInstance)
    buildTamperer = staticmethod(buildTamperer)
    createTamperer = staticmethod(createTamperer)
    parseConfig = staticmethod(parseConfig)

