from aiogeoip import (requests_geoip as geoip)
from addr import IPs
import pprint
import socket

pp = pprint.PrettyPrinter(width=41, compact=True, indent=2)


def usage_geoip(IPs, verbose=False):

    for ip in IPs:
        geo = geoip(ip)

        print(f'[+] o endereço do IP {ip} fica em:\n\t{geo.address}')

        if verbose:
            pp.pprint(geo)


if __name__ == '__main__':
    usage_geoip(IPs, False)
