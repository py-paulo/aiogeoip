"""
The API limits the number of requests per minute, you must do the
control on your own. What we do is a basic task but does not
guarantee the correct functioning of your software.
"""
import urllib.request
import json
import time
import logging

from aiogeoip.model import Geolocation
from aiogeoip.geoip import uribase, query
from aiogeoip.utils import create_obj_geolocation


def _get(uri: str, attempts: int, max_attempts: int, time_sleep: int) -> dict:
    """Synchronous GET request to IP-API with JSON response

    Args:
        uri (str): complete URL
        attempts (int): number of attempts already made
        max_attempts (int): maximum attempts
        time_sleep (int): waiting time between attempts

    Returns:
        dict: json to dict with geolocation
    """
    if attempts == max_attempts:
        return None

    req = urllib.request.Request(uri)

    try:
        with urllib.request.urlopen(req) as response:
            body = response.read().decode('utf-8', errors='ignore')
            return json.loads(body)
    except urllib.error.HTTPError:
        logging.debug(('the user has sent many orders in a given '
                       'period of time. sleep two seconds.'))
    except TimeoutError:
        logging.debug(('connection failed because the connected '
                       'component did not respond correctly after '
                       'a period of time'))
    except Exception as err:
        logging.warning(f'not cataloged error: {err}')
    time.sleep(time_sleep)

    return _get(uri, attempts + 1, max_attempts, time_sleep)


def geoip(ip: str, attempts=0, max_attempts=3, time_sleep=2) -> Geolocation or None:
    """Geolocation object from an IP address

    Args:
        ip (str): ipv4
        attempts (int): number of attempts already made
        max_attempts (int): maximum attempts
        time_sleep (int): waiting time between attempts

    Returns:
        Geolocation or None: obj geolocation
    """
    uri = f'{uribase}{ip}{query}'

    geo = _get(uri, attempts, max_attempts, time_sleep)
    addr = create_obj_geolocation(geo)

    return addr
