import unittest
from aiogeoip import Cache
from collections import namedtuple


class CacheTest(unittest.TestCase):

    def test_already_exists(self):
        cache = Cache()

        Geoip = namedtuple('Geoip', 'ip attrs')

        IPs = [
            Geoip(ip='10.0.0.1', attrs='attrs'),
            Geoip(ip='10.0.0.2', attrs='attrs'),
            Geoip(ip='10.0.0.3', attrs='attrs'),
            Geoip(ip='10.0.0.1', attrs='attrs'),
            Geoip(ip='10.0.0.2', attrs='attrs'),
            Geoip(ip='10.0.0.5', attrs='attrs')
        ]

        item = cache.get(IPs[0])
        self.assertIsNone(item)

        cache.append(IPs[0])
        item = cache.get(IPs[0].ip)
        self.assertIsNotNone(item)

        for ip in IPs[1:]:
            # logic will only add items that do not exist
            if cache.get(ip.ip) is None:
                cache.append(ip)

        # as it has 2 repeated items the total size will be four items
        self.assertTrue(len(cache.dq) == 4)
