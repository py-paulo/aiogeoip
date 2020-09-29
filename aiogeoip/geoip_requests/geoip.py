import requests
from aiogeoip.model import Geolocation
from aiogeoip.geoip import uribase, query
from aiogeoip.utils import create_obj_geolocation


def _get(uri: str) -> dict:
    """Synchronous GET request to IP-API with JSON response

    Args:
        uri (str): url with query

    Returns:
        dict: raw geolocation
    """
    r = requests.get(uri)
    return r.json()


def geoip(ip: str) -> Geolocation or None:
    """Geolocation object from an IP address

    Args:
        ip (str): ipv4

    Returns:
        Geolocation or None: obj geolocation
    """
    uri = f'{uribase}{ip}{query}'

    geo = _get(uri)
    addr = create_obj_geolocation(geo)

    return addr
