import urllib.request
import json
import logging

from aiogeoip.model import Geolocation
from aiogeoip.geoip import uribase, query
from aiogeoip.utils import create_obj_geolocation


def _get(uri: str, attempts=0, max_attempts=3, sleep_time=2) -> dict:
    """Synchronous GET request to IP-API with JSON response

    Args:
        uri (str): url with query

    Returns:
        dict: raw geolocation
    """
    if attempts == max_attempts:
        return None

    req = urllib.request.Request(uri)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8', errors='ignore')
            data = json.loads(body)

            return data
    except urllib.error.HTTPError:
        logging.debug(('the user has sent many orders in a given'
                       'period of time. sleep two seconds.'))
    except TimeoutError:
        logging.debug(('connection failed because the connected '
                       'component did not respond correctly after '
                       'a period of time'))
    except Exception as err:
        logging.warning(f'not cataloged error: {err}')

    time.sleep(sleep_time)

    return _get(uri, attempts + 1)


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
