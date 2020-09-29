import unittest
import socket
from aiogeoip import requests_geoip as geoip


class RequestsGeoIPTest(unittest.TestCase):

    def test_geoip(self):
        valid_addresses = [
            socket.gethostbyname('www.google.com'),
            socket.gethostbyname('www.facebook.com'),
            socket.gethostbyname('www.github.com'),
            socket.gethostbyname('www.youtube.com')
        ]

        invalid_addresses = [
            '172.31.1.17',
            '192.168.1.1',
            '225.255.255.255',
            '10.0.0.100',
        ]

        for ip in valid_addresses:
            self.assertIsNotNone(geoip(ip))
            self.assertEqual(len(geoip(ip)), 19)

        for ip in invalid_addresses:
            self.assertIsNone(geoip(ip))
