from .geoip import (geoip as aiogeoip)
from .cache import Cache


class AioGeoIP:

    def __init__(self):
        self.cache = Cache()

    async def geoip(self, ip):
        geo = self.cache.get(ip)

        geo = await aiogeoip(ip) if geo is None else geo

        if geo is not None:
            self.cache.append(geo)

        return geo

    def geoips_in_cache(self):
        return [ip for ip in self.cache.dq]
