from .geoip import (geoip as aiogeoip)
from .cache import Cache
from .model import Geolocation
from typing import List


class AioGeoIP:
    """class for optimizing the use of Geolocation by IP
    """

    def __init__(self):
        self.cache = Cache()

    async def geoip(self, ip: str) -> Geolocation:
        """Checks whether a request has already been made
        to the IP before making a new one

        Args:
            ip (str): ipv4

        Returns:
            Geolocation: geoip
        """
        geo = self.cache.get(ip)

        geo = await aiogeoip(ip) if geo is None else geo

        if geo is not None:
            self.cache.append(geo)

        return geo

    def geoips_in_cache(self) -> List[Geolocation]:
        """Return all IPs in cache

        Returns:
            List[Geolocation]: all geoips
        """
        return [ip for ip in self.cache.dq]
