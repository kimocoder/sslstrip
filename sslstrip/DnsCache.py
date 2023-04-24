
class DnsCache:    

    '''
    The DnsCache maintains a cache of DNS lookups, mirroring the browser experience.
    '''

    _instance          = None

    def __init__(self):
        self.cache = {}

    def cacheResolution(self, host, address):
        self.cache[host] = address

    def getCachedAddress(self, host):
        return self.cache[host] if host in self.cache else None

    def getInstance():
        if DnsCache._instance is None:
            DnsCache._instance = DnsCache()

        return DnsCache._instance

    getInstance = staticmethod(getInstance)
