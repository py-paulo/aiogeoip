"""The API limits the number of requests per minute, you must do the
control on your own. What we do is a basic task but does not
guarantee the correct functioning of your software.

>>> import urllib.request
>>> import socket
>>> url_domains_example = ('https://raw.githubusercontent.com/'
...                        'py-paulo/aiogeoip/master/examples/domains.txt')
>>> with urllib.request.urlopen(url_domains_example) as response:
...     body = response.read().decode('utf-8', errors='ignore')
>>> lines = [line.lower() for line in body.split('\\n')]
>>> for line in lines:
...     try:
...         ip = socket.gethostbyname(line)
...         geo = geoip(ip)
...     except socket.gaierror:
...         pass
"""

import requests
import logging
import time
import socket

from typing import Tuple

from aiogeoip.model import Geolocation
from aiogeoip.geoip import uribase, query, uri_get_public_ip
from aiogeoip.utils import create_obj_geolocation


def _get(uri: str, attempts: int, max_attempts: int, time_sleep: int) -> dict:
    """Synchronous GET request to IP-API with JSON response

    Args:
        uri (str): complete URL
        attempts (int): number of attempts already made
        max_attempts (int): maximum attempts
        time_sleep (int): waiting time between attempts

    Returns:
        dict: raw geolocation
    """
    if attempts == max_attempts:
        return None

    try:
        r = requests.get(uri)

        if r.status_code == 200:
            return r.json()
        elif r.status_code == 429:
            logging.debug(('the user has sent many orders in a given '
                           'period of time. sleep two seconds.'))
        else:
            logging.warning('abnormal response code "%s".' % r.status_code)
    except requests.exceptions.ConnectionError:
        logging.debug(('the internet connection has been interrupted '
                       'or the server is no longer available.'))

    time.sleep(time_sleep)

    return _get(uri, attempts + 1, max_attempts, time_sleep)


def geoip(ip: str, attempts: int = 0, max_attempts: int = 3, time_sleep: int = 2) -> Geolocation or None:
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


def whoami() -> Tuple[str or None]:
    """Returns a Tuple with the public IPv4 address, private IPv4 and hostname.

    >>> info = whoami()
    >>> type(info[0])
    <class 'str'>
    >>> len(info)
    3

    Returns:
        Tuple[str or None]: public ip, private ip and hostname
    """
    hostname = socket.gethostname()
    private_ip = socket.gethostbyname(hostname)

    public_ip = None
    try:
        req = requests.get(uri_get_public_ip)
        public_ip = req.text
    except requests.exceptions.ConnectionError:
        logging.debug(('the internet connection has been interrupted '
                       'or the server is no longer available.'))
    except Exception as err:
        logging.warning('not cataloged error: %s' % err)

    return public_ip, private_ip, hostname
