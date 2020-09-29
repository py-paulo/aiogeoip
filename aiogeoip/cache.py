from collections import deque
from .model import Geolocation


class Cache:
    """Class to store geolocation in objects to avoid
    unnecessary queries and optimize the library

    Geolocation objects are stored and not the answers
    in json => dict of the request to the API
    """

    def __init__(self):
        self.dq = deque(maxlen=100)

    def get(self, ip: str) -> Geolocation or None:
        """Searches from an IP in the instance cache for a
        Geolocation object, if not found returns None

        Args:
            ip (str): ipv4

        Returns:
            Geolocation or None: geolocation
        """
        for item in self.dq:
            if item[0] == ip:
                return item[1]
        return None

    def append(self, geoip: Geolocation):
        self.dq.append((geoip.ip, geoip))
